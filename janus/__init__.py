import os
import sys


print('Loading janus')

if ( sys.platform == "win32" ):
    from janus_swi._find_swipl import swipl_properties
    props = swipl_properties()
    if ( props ):
        if ( int(props["PLVERSION"]) < 90112 ):
             raise RuntimeError("At least SWI-Prolog version 9.1.12 is required")
        libdir = os.path.dirname(props["PLLIBSWIPL"])
        os.add_dll_directory(libdir)
    else:
        raise RuntimeError("Could not find SWI-Prolog in %PATH% or registry")
print('from janus_swi.janus import *')
from janus_swi.janus import *
print('import janus_swi._swipl')
import janus_swi._swipl

print('Initializing swipl')
_swipl.initialize("swipl",
                  "-g", "true",
                  "--no-signals")

# Get library(janus) for calling Python from Prolog.  If this library is
# already part of Prolog, use it, else add this directory to the library
# search path.

print(f'Adding {os.path.dirname(__file__)} to library search path')
_swipl.call("(exists_source(library(janus))->true;(asserta(user:file_search_path(library, Here)),writeln(here=Here)))",
            {"Here":os.path.dirname(__file__)})
