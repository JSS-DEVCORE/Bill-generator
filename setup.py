application_title = 'BillGen'
main_python_file = 'Bill.py'

import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"
    
include = []
includefiles = ['Themes','Icons','Theme Backs','QRCodes','Bills','SQL Dump'] # include any files here that you wish


setup(
    name = application_title,
    version = "1.0",
    description = "A simple bill generating software",
    author = "Yashas, Raghav",
    options = {"build_exe": {"includes":include, "include_files":includefiles}},
    executables = [Executable(main_python_file, base = base, icon = 'Icons/BillGenIcon.ico')])

