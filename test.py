import subprocess

# Define the command to be executed
command = []
command.append(['python', './Image_Process_Scripts/image_blur.py', "./Input/",'2' ,'./Output/Test_blur_dir'])

# command.append(['python', './Image_Process_Scripts/image_resize_by_ref.py', './Input/Test_resize_by_ref_file_dir', './Output/Test_trim_dir'])
# command.append(['python', './Image_Process_Scripts/image_resize_by_ref.py', './i1.png', './Output/newsize/'])

# Execute the command
for cmd in command:
    subprocess.run(cmd)