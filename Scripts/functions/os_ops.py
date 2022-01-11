import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_notepad():
    os.startfile(paths['notepad'])

def open_calculator():
    sp.Popen(paths['calculator'])

