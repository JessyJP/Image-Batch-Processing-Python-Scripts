### ----------- Copy Right -----------
# Image Resizing Script
# Author: JessyJP
# Date: April 2, 2023
# Description: This script resizes the image(s) to the specified width and height.

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
from common_util import checkAndCreateDirectory, checkAndCreateDirectory_withFileName
from common_util import process_resize_images

# Get command line arguments
if len(sys.argv) < 4:
    print("Usage: python resize.py <width> <height> <image input directory or file-path> [image output directory or file-path]")
    sys.exit(1)
#end

width = int(sys.argv[1])
height = int(sys.argv[2])
input_fileOrPath = sys.argv[3]
output_fileOrPath = sys.argv[4] if len(sys.argv) >= 5 else None

# Call the main function
process_resize_images(width,height,input_fileOrPath,output_fileOrPath)