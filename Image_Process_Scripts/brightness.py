### ----------- Copy Right -----------
# Brightness Script
# Author: JessyJP
# Date: April 5, 2023
# Description: This script adjusts the brightness of an image.

# The script uses the Pillow library, which is licensed under the open-source PIL Software License:
# Permission to use, copy, modify and distribute PIL and its associated documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies.
# The script itself is licensed under the MIT License:
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software...

### ----------- Check requirements ----------- 
from common_util import check_and_install_required_packages

# List of required packages
required_packages = ['Pillow']

# Install any missing packages
check_and_install_required_packages(required_packages)


### ---------- Script section ----------- 
import os
import sys
from PIL import Image, ImageEnhance
from common_util import checkAndCreateDirectory , checkAndCreateDirectory_withFileName

# Get command line arguments
if len(sys.argv) < 3:
    print("Usage: python brightness.py <input_file_or_directory> <brightness_factor> [<output_file_or_directory>]")
    sys.exit(1)
#end

input_fileOrPath = sys.argv[1]
brightness_factor = float(sys.argv[2])
output_fileOrPath = sys.argv[3] if len(sys.argv) > 3 else None


# Define a function to adjust the brightness of a single image
def adjust_brightness(input_filename, output_filename, brightness_factor):
    # Load the image
    image = Image.open(input_filename)

    # Apply the brightness factor
    brightness = ImageEnhance.Brightness(image)
    adjusted_image = brightness.enhance(brightness_factor)

    # Save the adjusted image
    adjusted_image.save(output_filename)

    # Print message for the processed image
    print(f"Brightness: {input_filename} -> {output_filename}")
#end

# If input_fileOrPath is a directory, process all images in the directory
if os.path.isdir(input_fileOrPath):
    # Assign the relevant variables
    input_dir = input_fileOrPath;
    output_dir = output_fileOrPath;

    if output_dir is None:
        output_dir = input_dir
    #end
    checkAndCreateDirectory(output_dir)

    for filename in os.listdir(input_dir):
        input_filename = os.path.join(input_dir, filename)
        output_filename = os.path.join(output_dir, filename)

        # If output_dir is the same as the input directory, append '_adjusted' to the filename
        if input_dir == output_dir:
            output_filename = os.path.join(output_dir, os.path.splitext(filename)[0] + '_adjusted' + os.path.splitext(filename)[1])
        #end

        # Process the image, i.e. do brightness adjustment 
        adjust_brightness(input_filename, output_filename, brightness_factor)
    #end
    
else:
    # If a single image is supplied, just adjust that image
    # Assign the relevant variables
    input_filename = input_fileOrPath;
    if output_fileOrPath is None:
        output_filename = os.path.splitext(input_filename)[0] + "_adjusted" + os.path.splitext(input_filename)[1]
    else:
        output_filename = output_fileOrPath
    #end
    
    checkAndCreateDirectory_withFileName(output_filename)
        
    # Process the image
    adjust_brightness(input_filename, output_filename, brightness_factor)
#end