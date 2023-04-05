### ----------- Copy Right -----------
# Image Contrast Script
# Author: JessyJP
# Date: April 5, 2023
# Description: This script adjusts the contrast of an image.

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
    print("Usage: python contrast.py <input_file_or_directory> <contrast_value> [<output_file_or_directory>]")
    sys.exit(1)
#end

input_fileOrPath = sys.argv[1]
contrast_value = float(sys.argv[2])
output_fileOrPath = sys.argv[3] if len(sys.argv) > 3 else None


# Define a function to adjust contrast of a single image
def adjust_contrast(input_filename, output_filename, contrast_factor):
    # Load the image
    image = Image.open(input_filename)

    # Adjust the contrast of the image
    enhancer = ImageEnhance.Contrast(image)
    contrasted_image = enhancer.enhance(contrast_factor)

    # Save the contrasted image
    contrasted_image.save(output_filename)

    # Print message for the processed image
    print(f"Contrast adjusted: {input_filename} -> {output_filename}")
#end


# If input_fileOrPath is a directory, process all images in the directory
if os.path.isdir(input_fileOrPath):
    # Assign the relevant variables
    input_dir = input_fileOrPath
    output_dir = output_fileOrPath

    if output_dir is None:
        output_dir = input_dir
    #end

    checkAndCreateDirectory(output_dir)

    for filename in os.listdir(input_dir):
        input_filename = os.path.join(input_dir, filename)
        if os.path.isdir(input_filename):# Check if the file name is a directory
            continue; # TODO: recursion is needed here
        #end
        output_filename = os.path.join(output_dir, filename)

        # If output_dir is the same as the input directory, append '_contrasted' to the filename
        if input_dir == output_dir:
            output_filename = os.path.join(output_dir, os.path.splitext(filename)[0] + '_contrasted' + os.path.splitext(filename)[1])
        #end

        # Process the image, i.e. adjust contrast 
        adjust_contrast(input_filename, output_filename, contrast_value)
    #end
    
else:
    # If a single image is supplied, just adjust contrast of that image
    # Assign the relevant variables
    input_filename = input_fileOrPath;
    if output_fileOrPath is None:
        output_filename = os.path.splitext(input_filename)[0] + "_contrasted" + os.path.splitext(input_filename)[1]
    else:
        output_filename = output_fileOrPath
    #end

    checkAndCreateDirectory_withFileName(output_filename)
        
    # Process the image
    adjust_contrast(input_filename, output_filename, contrast_value)
#end
