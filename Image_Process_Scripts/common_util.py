import sys
import os
import subprocess


# Global Disable switch
PackageInstallCheck_Enabled = False

def check_and_install_required_packages(package_list):
    """Checks if the required packages are installed and installs them if they are not."""
    
    if PackageInstallCheck_Enabled:# Disable check and do nothing
        return "PackageInstallCheck is Disabled";
    #end
    
    # Check if each package is installed
    missing_packages = []
    for package in package_list:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
        #end
    #end
    
    # Install any missing packages using pip
    if missing_packages:
        print(f"Installing missing packages: {', '.join(missing_packages)}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing_packages])
    #end
    
#end

def checkAndCreateDirectory(output_path):
    # If an input directory is supplied, check for an output directory
    # Create the output directory if it doesn't exist
    if output_path is not None:        
        # To avoid errors make sure there is always a forward slash at the end
        if output_path != '' and not output_path.endswith('/'):
            output_path += '/'
        #end
        
        # Conversion to dirname
        output_dir = os.path.dirname(output_path)          
        # Create the directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        #end
    #end
#end