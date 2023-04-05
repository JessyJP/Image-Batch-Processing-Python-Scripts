### ----------- Copy Right ----------- 
# Image Trimming Script
# Author: JessyJP
# Date: April 2, 2023
# Description: This script trims the specified number of pixels from the top, bottom, left, and right sides of an image or a directory of images.

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
from PIL import Image
import sys
import os
from common_util import checkAndCreateDirectory , checkAndCreateDirectory_withFileName

# Get command line arguments
if len(sys.argv) < 6:
    print("Usage: python trim.py <top pixels> <bottom pixels> <left pixels> <right pixels> <image input directory or file-path> [image output directory or file-path] ")#[image extension]
    sys.exit(1)
#end

top_pixels = int(sys.argv[1])
bottom_pixels = int(sys.argv[2])
left_pixels = int(sys.argv[3])
right_pixels = int(sys.argv[4])
input_fileOrPath = sys.argv[5]
output_fileOrPath = sys.argv[6] if len(sys.argv) >= 7 else None
# image_extension = sys.argv[7] if len(sys.argv) >= 8 else None

# Define function to trim an individual image
def trim_image(input_filename, output_filename):
    # Load the image
    image = Image.open(input_filename)

    # Trim the image
    width, height = image.size
    box = (left_pixels, top_pixels, width - right_pixels, height - bottom_pixels)
    trimmed_image = image.crop(box)

    # Save the trimmed image
    trimmed_image.save(output_filename)

    # Print message for the processed image
    print(f"Trim: {input_filename} -> {output_filename}")
#end


# Trim all images in a directory or a specific type of image
if os.path.isdir(input_fileOrPath):
    # Assign the relevant variables
    input_dir = input_fileOrPath;
    output_dir = output_fileOrPath;
    
    checkAndCreateDirectory(output_dir)        
            
    # If an input directory is supplied, trim all images in the directory one by one
    for filename in os.listdir(input_dir):
        # if image_extension is None or filename.endswith(image_extension):
        input_filename = os.path.join(input_dir, filename)
        if os.path.isdir(input_filename):# Check if the file name is a directory
            continue; # TODO: recursion is needed here
        #end
        if output_dir is None:
            output_filename = os.path.splitext(input_filename)[0] + "_trimmed" + os.path.splitext(input_filename)[1]
        else:
            output_filename = os.path.join(output_dir, filename)
        
        # Do the trimming    
        trim_image(input_filename, output_filename)
    #end
        
else:
    # If a single image is supplied, just trim that image
    # Assign the relevant variables
    input_filename = input_fileOrPath;
    if output_fileOrPath is None:
        output_filename = os.path.splitext(input_filename)[0] + "_trimmed" + os.path.splitext(input_filename)[1]
    else:
        output_filename = output_fileOrPath;
    #end
    
    checkAndCreateDirectory_withFileName(output_filename)
        
    # Do the trimming
    trim_image(input_filename, output_filename)
#end