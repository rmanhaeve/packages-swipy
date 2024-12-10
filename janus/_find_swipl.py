import os
import sys
import subprocess
import re
import pathlib

def swipl_properties(exe="swipl"):
    try:
        return swipl_exe_properties(exe)
    except:
        exe = find_swipl()
        if ( exe ):
            return swipl_exe_properties(exe)
        return None
    
def swipl_exe_properties(exe="swipl"):
    config = subprocess.run([exe, '--dump-runtime-variables'],
                            stdout=subprocess.PIPE).stdout.decode('utf-8')
    props = {}
    for line in config.splitlines():
        i = line.find("=")      # line is name="value";
        name = line[0:i]
        value = line[i+2:-2]
        props[name] = value;
    return props

def find_swipl():
    home = os.path.abspath('./bundled_swipl/')
    executable = "swipl"
    print('Bundled home directory:', home)
    if (not os.path.exists(home)):
        print(home, 'does not exist.')
        if ( sys.platform == "win32" ):
            home = _win32_home_from_registry()
            executable = "swipl.exe"
        else:
            home = None
    if ( home ):
        return os.path.join(home, "bin", executable)
    return None

def _win32_home_from_registry():
    reg = subprocess.run(["reg", 'query',
                          r'HKEY_LOCAL_MACHINE\Software\SWI\Prolog',
                          '/v', 'home'],
                         stdout=subprocess.PIPE).stdout.decode('utf-8')
    for line in reg.splitlines():
        match = re.match(r"\s*home\s+REG_SZ\s+(.*)$", line)
        if ( match ):
            return match.group(1)
    return None
