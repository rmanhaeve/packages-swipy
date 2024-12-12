# Build janus as a Python package

import os

SWIPL=os.getenv("SWIPL") or "swipl"
PLLIB="swipl"

from setuptools import setup, Extension
import sys
sys.path.append("janus")
from _find_swipl import swipl_properties

props=swipl_properties(SWIPL)

if ( not props ):
    raise RuntimeError("Failed to find SWI-Prolog components")
if ( int(props["PLVERSION"]) < 90112 ):
    raise RuntimeError("At least SWI-Prolog version 9.1.12 is required")

link_args=[]
if ( sys.platform == 'linux' ):
    link_args.append("-Wl,-rpath,$ORIGIN/bundled_swipl/lib/swipl/lib/x86_64-linux,--enable-new-dtags")
elif ( sys.platform == 'darwin' ):
    link_args.append(f'-Wl,-rpath,{props["PLLIBDIR"]}')
elif ( sys.platform == 'win32' ):
    PLLIB="libswipl"
print('link_args', link_args)
setup(name='janus_swi',
      version='1.5.0',
      description="Janus library to call SWI-Prolog",
      author="Jan Wielemaker",
      author_email="jan@swi-prolog.org",
      url="https://github.com/SWI-Prolog/packages-swipy",
      license="BSD-2",
      packages=['janus_swi'],
      package_dir={"janus_swi":"janus"},
      package_data={"janus_swi": ['janus.pl','bundled_swipl/**/*']},
      exclude_package_data={"janus_swi": ['bundled_swipl/**/*.so.*']},
      include_package_data=True,
      ext_modules= [
          Extension('janus_swi._swipl',
                    ['janus/janus.c'],
                    depends=[
                        'janus/hash.c',
                        'janus/mod_swipl.c'
                    ],
                    define_macros=[
                        ('PYTHON_PACKAGE', '1')
                    ],
                    include_dirs=[
                        f'{props["PLBASE"]}/include'
                    ],
                    extra_link_args=link_args,
                    library_dirs=[props["PLLIBDIR"]],
#                    runtime_library_dirs=["janus/bundled_swipl/lib/swipl/lib/x86_64-linux"],
                    libraries=[PLLIB])
          ])
