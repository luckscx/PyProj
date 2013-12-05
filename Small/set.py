import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["random","string"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).


setup(  name = "guess",
        version = "0.1",
        description = "My guess application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("guess.py")])

    