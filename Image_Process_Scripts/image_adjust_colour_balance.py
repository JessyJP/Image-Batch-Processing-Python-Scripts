### ----------- Copy Right -----------
# Adjust Color Balance Script
# Author: JessyJP
# Date: April 2, 2023
# Description: This script adjusts the color balance of an image.

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
from PIL import Image, ImageOps
import sys
import os
from common_util import checkAndCreateDirectory

# Get command line arguments
if len(sys.argv) < 4:
    print("Usage: python color_balance.py <red_shift> <green_shift> <blue_shift> <image input directory or file-path> [image output directory or file-path]")
    sys.exit(1)

red_shift = int(sys.argv[1])
green_shift = int(sys.argv[2])
blue_shift = int(sys.argv[3])
input_fileOrPath = sys.argv[4]
output_fileOrPath = sys.argv[5] if len(sys.argv) >= 6 else None

# Define function to adjust color balance of an individual image
def adjust_color_balance(input_filename, output_filename):
    # Load the image
    image = Image.open(input_filename)

    # Adjust color balance
    color_balanced_image = ImageOps.colorize(image.convert("L"), black=(0, 0, 0), white=(red_shift, green_shift, blue_shift))

    # Save the color balanced image
    color_balanced_image.save(output_filename)

    # Print message for the processed image
    print(f"Adjust Color Balance: {input_filename} -> {output_filename}")


# Adjust color balance of all images in a directory or a specific type of image
if os.path.isdir(input_fileOrPath):
    # Assign the relevant variables
    input_path = input_fileOrPath;
    output_path = output_fileOrPath;
    
    checkAndCreateDirectory(output_path)
            
    # If an input directory is supplied, adjust color balance of all images in the directory one by one
    for filename in os.listdir(input_path):
        input_filename = os.path.join(input_path, filename)
        if output_path is None:
            output_filename = os.path.splitext(input_filename)[0] + "_color_balanced" + os.path.splitext(input_filename)[1]
        else:
            output_filename = os.path.join(output_path, filename)
        
        # Do the color balancing    
        adjust_color_balance(input_filename, output_filename)
        
else:
    # If a single image is supplied, just adjust the color balance of that image
    # Assign the relevant variables
    input_filename = input_fileOrPath;
    if output_fileOrPath is None:
        output_filename = os.path.splitext(input_filename)[0] + "_color_balanced" + os.path.splitext(input_filename)[1]
    else:
        output_filename = output_fileOrPath;
    # Do the color balancing
    adjust_color_balance(input_filename, output_filename)
