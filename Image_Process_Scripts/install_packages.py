import subprocess
import sys

disable = True

def check_and_install_required_packages(package_list):
    """Checks if the required packages are installed and installs them if they are not."""
    
    if disable:# Disable check
        return "Disable Check";
    
    # Check if each package is installed
    missing_packages = []
    for package in package_list:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    # Install any missing packages using pip
    if missing_packages:
        print(f"Installing missing packages: {', '.join(missing_packages)}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing_packages])
