### ----------- Copy Right -----------
# Blur Script
# Author: 
# Date: April 5, 2023
# Description: This script blurs an image.

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
from PIL import Image, ImageFilter
from common_util import checkAndCreateDirectory , checkAndCreateDirectory_withFileName

# Get command line arguments
if len(sys.argv) < 3:
    print("Usage: python blur.py <output_file_or_directory> <input_file_or_directory> [blur_radius_1] [blur_radius_2] ...")
    sys.exit(1)

output_fileOrPath = sys.argv[1]
input_fileOrPath = sys.argv[2]
blur_radius = int(sys.argv[3])

# If output_fileOrPath is a directory, make sure it exists
if os.path.isdir(output_fileOrPath):
    checkAndCreateDirectory(output_fileOrPath)

# Define a function to blur a single image
def blur_image(input_filename, output_filename, blur_radius):
    # Load the image
    image = Image.open(input_filename)

    # Apply the blur filter
    blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))

    # Save the blurred image
    blurred_image.save(output_filename)

    # Print message for the processed image
    print(f"Blur: {input_filename} -> {output_filename}")
#end

# If input_fileOrPath is a directory, process all images in the directory
if os.path.isdir(input_fileOrPath):
    input_dir = input_fileOrPath
    output_dir = output_fileOrPath

    checkAndCreateDirectory(output_dir)
    
    for filename in os.listdir(input_dir):
        input_filename = os.path.join(input_dir, filename)
        output_filename = os.path.join(output_dir, filename)


        # If output_dir is the same as the input directory, append '_blurred' to the filename
        if input_dir == output_dir:
            output_filename = os.path.join(output_fileOrPath, os.path.splitext(filename)[0] + '_blurred' + os.path.splitext(filename)[1])
        #end
        
        # Process the image
        blur_image(input_filename, output_filename, blur_radius)
    #end

# If input_fileOrPath is a file, process that file only
else:
    input_filename = input_fileOrPath
    output_filename = output_fileOrPath

    # Process the image
    blur_image(input_filename, output_filename, blur_radius)
#end
