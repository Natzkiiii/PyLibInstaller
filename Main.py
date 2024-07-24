import subprocess
import sys

def InstReq(): # defines the function that ibstalls the requirements
    libs = ["pyautogui", "keyboard"] #define the libraries here
    # Install all required libraries in one subprocess call
    subprocess.check_call([sys.executable, "-m", "pip", "install", *libs])

    # the subprocess will type "Python.exe -m pip install" and then your libraries

# Install required libraries
instReq()
