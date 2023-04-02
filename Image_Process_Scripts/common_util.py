import sys
import os

def checkAndCreateDirectory(output_path):
    # If an input directory is supplied, check for an output directory
    # Create the output directory if it doesn't exist
    if output_path is not None:        
        # To avoid errors make sure there is always a forward slash at the end
        if output_path != '' and not output_path.endswith('/'):
            output_path += '/'
        #end
        
        # Conversion to dirname
        output_dir = os.path.dirname(output_path)          
        # Create the directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        #end
    #end
#end