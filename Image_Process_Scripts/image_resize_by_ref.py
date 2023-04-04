### ----------- Copy Right -----------
# Image Resizing by Reference Script
# Author: JessyJP
# Date: April 2, 2023
# Description: This script resizes the image(s) to the same size as the reference image(s).

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
import subprocess
from common_util import checkAndCreateDirectory, checkAndCreateDirectory_withFileName
from common_util import process_resize_images


# Get command line arguments
if len(sys.argv) < 3:
    print("Usage: python image_resize.py <image reference directory or file-path> <image input directory or file-path> [image output directory or file-path]")
    sys.exit(1)
#end

ref_fileOrPath = sys.argv[1]
input_fileOrPath = sys.argv[2]
output_fileOrPath = sys.argv[3] if len(sys.argv) >= 4 else None

# Expect that the input and output 
if output_fileOrPath is None:
    output_fileOrPath = '';
#end

# Determine the reference image size
if os.path.isdir(ref_fileOrPath):
    # case: dir - dir - dir # That should be done file by file
    if os.path.isdir(input_fileOrPath):
        # The input is confirmed to be a directory
        input_dir = input_fileOrPath
        # Also check the output path
        if output_fileOrPath is None or output_fileOrPath == '':
            output_dir = input_fileOrPath
        else:
            output_dir = output_fileOrPath
        #end
        
        raise NotImplementedError("Case not implemented")
        
        # If a reference directory is supplied, find the reference images and process the images one to one
        for filename in os.listdir(ref_fileOrPath):
            ref_image = Image.open(filename)
            ref_width, ref_height = ref_image.size
            
            # Construct filenames
            input_filename  = os.path.join(input_dir, filename)                
            output_filename = os.path.join(output_dir, filename)
            if input_filename == output_filename:
                output_filename = os.path.splitext(input_filename)[0] + _suffix + os.path.splitext(input_filename)[1]
            # end
            
            # Run the resize call
            process_resize_images(ref_width,ref_height,input_filename,output_filename,"_resized_by_ref","Resize by ref")
            

        #end
    else:
        # TODO: # case: dir - file - file(s)/Dir
        raise NotImplementedError("Case not implemented")
    #end
    
else:
    # case: file - dir/file - dir/file
    # If a single reference image is supplied, just get its size
    ref_image = Image.open(ref_fileOrPath)
    ref_width, ref_height = ref_image.size

    # Run the resize call
    process_resize_images(ref_width,ref_height,input_fileOrPath,output_fileOrPath,"_resized_by_ref","Resize by ref")
#end
