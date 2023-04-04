### ----------- Copy Right ----------- 
# Image Auto Color Balance Script
# Author: JessyJP
# Date: April 4, 2023
# Description: This script does auto color balance on an image or a directory of images.

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
from PIL import Image, ImageOps, ImageStat
import sys
import os
from common_util import checkAndCreateDirectory

# Get command line arguments
if len(sys.argv) < 2:
    print("Usage: python image_color_balance.py <image input directory or file-path> [image output directory or file-path]")
    sys.exit(1)

input_fileOrPath = sys.argv[1]
output_fileOrPath = sys.argv[2] if len(sys.argv) >= 3 else None

from PIL import Image, ImageOps, ImageStat

def image_color_balance(input_filename, output_filename):
    """
    Auto-Adjusts color balance of an individual image.

    Args:
        input_filename (str): The path to the input image file.
        output_filename (str): The path to save the output image file.

    Returns:
        None
    """
    # Load the image
    image = Image.open(input_filename)

    # Convert the image to the RGB mode if it's not already in that mode
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Apply autocontrast and equalize
    image = ImageOps.autocontrast(ImageOps.equalize(image), cutoff=1)

    # Split the image into red, green, and blue bands
    r, g, b = image.split()

    # Calculate the average pixel value for each band
    r_avg = ImageStat.Stat(r).mean[0]
    g_avg = ImageStat.Stat(g).mean[0]
    b_avg = ImageStat.Stat(b).mean[0]

    # Calculate the scaling factor for each band
    r_scale = 128 / r_avg if r_avg > 0 else 1
    g_scale = 128 / g_avg if g_avg > 0 else 1
    b_scale = 128 / b_avg if b_avg > 0 else 1

    # Apply the scaling factor to each band
    r = r.point(lambda i: i * r_scale)
    g = g.point(lambda i: i * g_scale)
    b = b.point(lambda i: i * b_scale)

    # Merge the bands into a new RGB image
    color_balanced_image = Image.merge("RGB", (r, g, b))

    # Save the adjusted image
    color_balanced_image.save(output_filename)

    # Print message for the processed image
    print(f"Auto Color Balance:{input_filename} -> {output_filename}")

#end



# Auto-Adjust color balance of all images in a directory or a specific type of image
if os.path.isdir(input_fileOrPath):
    # Assign the relevant variables
    input_path = input_fileOrPath
    output_path = output_fileOrPath or input_path
    
    checkAndCreateDirectory(output_path)
            
    # If an input directory is supplied, auto-adjust color balance of all images in the directory one by one
    for filename in os.listdir(input_path):
        input_filename = os.path.join(input_path, filename)
        if output_fileOrPath is None:
            output_filename = os.path.join(input_path, f"{os.path.splitext(filename)[0]}_auto_color_balanced{os.path.splitext(filename)[1]}")
        else:
            output_filename = os.path.join(output_path, filename)
        
        # Auto-Adjust color balance    
        image_color_balance(input_filename, output_filename)
        
else:
    # If a single image is supplied, just auto-adjust color balance of that image
    # Assign the relevant variables
    input_filename = input_fileOrPath
    if output_fileOrPath is None:
        output_filename = os.path.join(os.path.dirname(input_filename), f"{os.path.splitext(os.path.basename(input_filename))[0]}_auto_color_balanced{os.path.splitext(os.path.basename(input_filename))[1]}")
    else:
        output_filename = output_fileOrPath
    
    # Auto-Adjust color balance
    image_color_balance(input_filename, output_filename)