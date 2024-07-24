import subprocess
import sys

def install_libraries():
    with open('requirements.txt', 'r') as f:
        required_libraries = f.read().splitlines()
    # Install all required libraries in one subprocess call
    subprocess.check_call([sys.executable, "-m", "pip", "install", *required_libraries])

# Install required libraries
install_libraries()
