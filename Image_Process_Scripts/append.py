### ----------- Copy Right -----------
# Image Appending Script
# Author: JessyJP
# Date: April 2, 2023
# Description: This script appends the image(s) horizontally.

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
from common_util import checkAndCreateDirectory

# Get command line arguments
if len(sys.argv) < 5:
    print("Usage: \n\
                  case 1: python append.py <append direction> <output file-path> <input image file-paths>    OR \n\
                  case 2: python append.py <append direction> <output directory> <input image directories>   (assume the same filename is found in each directory OR \n\
                  case 3: python append.py <append direction> <output file-path> <input image file-path> <repeat count>    OR \n\
                  case 4: python append.py <append direction> <output directory> <input directory> <repeat count>       \n \n \
                  append direction is -h or -v \
                  append direction without interruption is -hc or -vc ")
    sys.exit(1)
#end

append_direction = sys.argv[1].lower()
continueFileProcessing  = False;
if "c" in append_direction:
    continueFileProcessing  = True;
    append_direction.replace("c", "")
#end

output_fileOrPath = sys.argv[2]
input_fileOrPath = sys.argv[3]
# Determine the call case is multiple input files:
if len(sys.argv) > 4 and not sys.argv[4].isdigit():
    repeat_count = 0
else: # There is a repeat count
    repeat_count = 1 if len(sys.argv) < 5 else int(sys.argv[4])
#end
  
# Define function to append multiple images horizontally
def append_images_horizontally(input_filenames, output_filename, repeat_count=0):
    # Load all image filenames
    loaded_images = [Image.open(image_path) for image_path in input_filenames]

    # Repeat the images if repeat_count is greater than 1
    arrow = "->"
    if repeat_count > 1:
        loaded_images *= repeat_count
        arrow = "x"+ str(repeat_count)+arrow
    #end
    
    # Calculate the final image size
    max_height = max(img.height for img in loaded_images)
    total_width = sum(img.width for img in loaded_images)

    
    # Create the new image
    new_image = Image.new('RGB', (total_width, max_height))
    
    # Append all images horizontally
    current_x = 0
    for image in loaded_images:
        new_image.paste(image, (current_x, 0))
        current_x += image.width
    #end
        
    # Save the new image
    new_image.save(output_filename)
    
    # Print message for the processed images
    print(f"Append Horizontally: {input_filenames} {arrow} {output_filename}")
#end    

# Define function to append multiple images vertically
def append_images_vertically(input_filenames, output_filename,repeat_count=0):
    # Load all image filenames
    loaded_images = [Image.open(image_path) for image_path in input_filenames]
    
    # Repeat the images if repeat_count is greater than 1
    arrow = "->"
    if repeat_count > 0:
        loaded_images *= repeat_count
        arrow = "x"+ str(repeat_count)+arrow
    #end
    
    # Calculate the final image size
    max_width    = max(img.width for img in loaded_images)
    total_height = sum(img.height for img in loaded_images)
    
    # Create the new image
    new_image = Image.new('RGB', (max_width, total_height))
    
    # Append all images vertically
    current_y = 0
    for image in loaded_images:
        new_image.paste(image, (0, current_y))
        current_y += image.height
    
    # Save the new image
    new_image.save(output_filename)
    
    # Print message for the processed images
    print(f"Append Vertially: {input_filenames} {arrow} {output_filename}")
#end

# Direction dispatcher 
def append_images(input_filenames, output_filename, repeat_count=0):
    if append_direction == "-h":
        append_images_horizontally(input_filenames, output_filename, repeat_count)
    else:
        append_images_vertically(input_filenames, output_filename,repeat_count)
    #end
#end


# Append all image in a list of input image file paths for case 1: or the same filename from each directory case 2:
if repeat_count == 0:
    output_filename = output_fileOrPath
    input_fileOrPath = []
    for arg in sys.argv[3:]:
        input_fileOrPath.append(arg)
    #end
    
    assumeAllInputsArePaths = True
    for checkPath in input_fileOrPath:
        if not checkPath.endswith('/'):
            checkPath += '/'
        #end
        checkPath = os.path.dirname(checkPath)# convert ot dirname
        # This condition will check if all of the 
        if not os.path.isdir(checkPath) or not os.path.exists(checkPath):
            assumeAllInputsArePaths = False
        #end
    #end
 
 
    if assumeAllInputsArePaths: # Case 2
        input_paths = input_fileOrPath
        output_path = output_fileOrPath
        
        checkAndCreateDirectory(output_path)
        
        # If number of input directories are supplied, append all images with the same name in each directory
        for filename in os.listdir(input_paths[0]):
            allFilesChecked = True
            input_filepaths = []
            for p in range(len(input_paths)):
                input_filepaths.append(os.path.join(input_paths[p], filename))
                if not (os.path.exists(input_filepaths[p]) and os.path.isfile(input_filepaths[p])):
                    print(f" *Missing File Error: File in filepath [ {input_filepaths[p]} ] does not exist!!!")
                    if continueFileProcessing:
                        sys.exit(1)
                    else:
                        allFilesChecked = False
                    #end
                #end
            #end
            
            output_filename = os.path.join(output_path, filename) 
            if (os.path.exists(output_filename) and os.path.isfile(output_filename)):
                output_filename = os.path.splitext(output_filename)[0] + "_combined" + os.path.splitext(output_filename)[1]
            #end

            if not allFilesChecked:# If there is an error with the files go to the next set
                print(f" *Skip Output File Error: File in filepath [ {output_filename} ] not created due to missing parts!!!")
                continue
            #end

            append_images(input_filepaths, output_filename,0)                
        #end
    
    else: # Case 1
        # Not all inputs arguments are valid directories therefore they must be file-paths
        input_filenames = input_fileOrPath
        output_filename = output_fileOrPath

        append_images(input_filenames, output_filename,repeat_count)
    #end

else:
    # Self Append all images from a single directory case 4:
    if os.path.isdir(input_fileOrPath):
        # Assign the relevant variables
        input_path = input_fileOrPath
        output_path = output_fileOrPath
        
        checkAndCreateDirectory(output_path)
                
        # If an input directory is supplied, append all images in the directory
        for filename in os.listdir(input_path):
            input_filename = os.path.join(input_path, filename)
            if input_path == output_path:
                output_filename = os.path.splitext(input_filename)[0] + "_combined" + os.path.splitext(input_filename)[1]
            else:
                output_filename = os.path.join(output_path, filename) 
            #end
            append_images([input_filename], output_filename,repeat_count)                
        #end
            
    else:
        # If a single image is supplied, just self append that image the number of times case 3:
        output_filename = output_fileOrPath;
        # Assign the relevant variables
        input_filename = input_fileOrPath;
        # Do append images
        append_images([input_filename], output_filename,repeat_count)
    #end
#end