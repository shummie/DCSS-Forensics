import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"silent": ["s"], "create_shared_zip" : False, "include_files":["config.ini"]}
#buildOptions = dict(create_shared_zip = False, silent = ["s"])

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "DCSSForensics",
        version = "0.03",
        description = "DCSS Forensics",
        options = {"build_exe": build_exe_options},
        #options = dict(build_exe = buildOptions),
        executables = [Executable("forensicsMain.py", base=base, appendScriptToExe=True, appendScriptToLibrary=False, 
                                  targetName = "DCSSForensics.exe", compress = True)])

# To create executable, run the following on the command prompt in the main directory
# python setup.py build
# Cx_Freeze needs to be installed. Also, the PATH variables may need to be modified.