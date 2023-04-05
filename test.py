import subprocess

# Define the command to be executed
command = []
command.append(['python', './Image_Process_Scripts/contrast.py', "./Input/FX_08_VirtualDrummerSolid.png" ,"0.7","./Output/Test_autobalance_file.png"])

# Execute the command
for cmd in command:
    subprocess.run(cmd)