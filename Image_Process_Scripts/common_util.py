import sys
import os
import subprocess


# Global Variables
PackageInstallCheck_Disabled = True

## ============= Package Install Section =============

def check_and_install_required_packages(package_list):
    # Checks if the required packages are installed and installs them if they are not.
    
    if PackageInstallCheck_Disabled:# Disable check and do nothing
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

## ============= Directory Check and Make Section =============

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
            print(f"Dir created: {output_dir}")
        #end
    #end
#end

def checkAndCreateDirectory_withFileName(output_filepath):
    # Get the directory path from the output file path
    output_dir = os.path.dirname(output_filepath)

    # Call the original function to create the directory
    checkAndCreateDirectory(output_dir)
#end


## ============= Image Processing Section =============
from PIL import Image

# Define function to resize an individual image
def resize_image(input_filename, output_filename,width, height,diagnostic_prefix):
    # Load the image
    image = Image.open(input_filename)

    # Resize the image
    resized_image = image.resize((width, height))

    # Save the resized image
    resized_image.save(output_filename)

    # Print message for the processed image
    print(f"{diagnostic_prefix}: {input_filename} -> {output_filename}")
#end

def process_resize_images(width,height,input_fileOrPath,output_fileOrPath,_suffix="_resized",diagnostic_prefix = "Resize"):
  
    # Check if the output dir is empty
    if output_fileOrPath == "" or output_fileOrPath == '':
        output_fileOrPath = None;
    #end
    
    # Resize all images in a directory or a specific type of image
    if os.path.isdir(input_fileOrPath):
        # Assign the relevant variables
        input_path = input_fileOrPath;
        output_path = output_fileOrPath;
        
        checkAndCreateDirectory(output_path)
                
        # If an input directory is supplied, resize all images in the directory one by one
        for filename in os.listdir(input_path):
            input_filename = os.path.join(input_path, filename)
            if output_path is None:
                output_filename = os.path.splitext(input_filename)[0] + _suffix + os.path.splitext(input_filename)[1]
            else:
                output_filename = os.path.join(output_path, filename)
            #end
            
            # Do the resizing    
            resize_image(input_filename, output_filename,width, height,diagnostic_prefix)
        #end
    else:
        # If a single image is supplied, just resize that image
        # Assign the relevant variables
        input_filename = input_fileOrPath;
        if output_fileOrPath is None:
            output_filename = os.path.splitext(input_filename)[0] + _suffix + os.path.splitext(input_filename)[1]
        else:
            output_filename = output_fileOrPath;
        #end
        
        checkAndCreateDirectory_withFileName(output_filename)
            
        # Do the resizing
        resize_image(input_filename, output_filename,width, height,diagnostic_prefix)
    #end
#end