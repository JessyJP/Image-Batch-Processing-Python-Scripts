### ----------- Copy Right -----------
# Alpha Blending Script
# Author: JessyJP
# Date: April 4, 2023
# Description: This script alpha blends one or more images.

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


# Define function to alpha blend two images
def alpha_blend(image1, image2, alpha):
    # Resize both images to the same size
    image1 = image1.resize(image2.size)
    # Alpha blend the two images
    blended_image = Image.blend(image1, image2, alpha)
    return blended_image


# Define function to alpha blend multiple images
def alpha_blend_multiple(input_files, output_filename):
    # Open the first image
    blended_image = Image.open(input_files[0]).convert("RGBA")
    # Iterate over the remaining images and alpha blend them with the previous image
    for i in range(1, len(input_files), 2):
        alpha = float(input_files[i])
        image = Image.open(input_files[i+1]).convert("RGBA")
        blended_image = alpha_blend(blended_image, image, alpha)
    # Save the final blended image
    blended_image.save(output_filename)

    # Print message for the processed image
    print(f"Alpha Blend: {input_files} -> {output_filename}")



# check if alpha blend is valid
def is_valid_alpha_blend(alpha_blend):
    try:
        alpha_blend = float(alpha_blend)
        if alpha_blend < 0 or alpha_blend > 1:
            return False
    except:
        return False
    return True

# check input arguments
if len(sys.argv) < 4:
    print("Usage: python alphablend.py <output_filepath>    <input_filepath1> <alpha_blend1> <input_filepath2> <alpha_blend2> ... OR")
    print("Usage: python alphablend.py <output_directory>   <input_directory> <alpha_blend> <input_filepath>")
    print("Usage: python alphablend.py <output_directories> <input_directories> <alpha_blend>")
    sys.exit(1)

# check case 1
if os.path.isfile(sys.argv[1]):
    output_file_path = sys.argv[1]
    input_paths = []
    alpha_blends = []
    for i in range(2, len(sys.argv), 2):
        if not is_valid_alpha_blend(sys.argv[i+1]):
            print("Error: Invalid alpha blend value")
            sys.exit(1)
        input_paths.append(sys.argv[i])
        alpha_blends.append(float(sys.argv[i+1]))
    if len(input_paths) < 2:
        print("Error: At least two input files are required for alpha blending")
        sys.exit(1)

# check case 2
elif os.path.isdir(sys.argv[1]):
    input_dir_path = sys.argv[1]
    output_dir_path = os.path.join(input_dir_path, "alphablended")
    if len(sys.argv) > 2:
        print("Warning: Extra arguments will be ignored in case of directory input")

# check case 3
else:
    output_dirs = []
    input_dirs = []
    alpha_blend = float(sys.argv[-1])
    for i in range(1, len(sys.argv)-1, 2):
        input_dir = sys.argv[i]
        output_dir = os.path.join(os.path.dirname(input_dir), os.path.basename(input_dir) + "_alphablended")
        if not os.path.isdir(input_dir):
            print("Error: Invalid input directory")
            sys.exit(1)
        input_dirs.append(input_dir)
        output_dirs.append(output_dir)
    if len(input_dirs) < 2:
        print("Error: At least two input directories are required for alpha blending")
        sys.exit(1)




output_fileOrPath = sys.argv[1]
input_files = sys.argv[2:]

# If only one input file is given, just copy it to the output file
if len(input_files) == 1:
    input_filename = input_files[0]
    output_filename = output_fileOrPath
    Image.open(input_filename).save(output_filename)
    print(f"{input_filename} -> {output_filename}")

# If more than one input file is given, alpha blend them into the output file
elif len(input_files) % 2 == 0:
    alpha_blend_multiple(input_files, output_fileOrPath)

# If the input is a directory, alpha blend all the images in that directory
elif os.path.isdir(input_files[0]):
    # Assign the relevant variables
    input_path = input_files[0]
    output_path = output_fileOrPath
    
    checkAndCreateDirectory(output_path)

    # If an input directory is supplied, alpha blend all images in the directory one by one
    for filename in os.listdir(input_path):
        input_filename = os.path.join(input_path, filename)
        output_filename = os
