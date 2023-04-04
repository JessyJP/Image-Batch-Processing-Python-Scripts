import subprocess

# Define the command to be executed
command = []
command.append(['python', './Image_Process_Scripts/auto_balance.py', "./Input/FX_08_VirtualDrummerSolid.png" ,"./Output/Test_autobalance_file.png"])

# Execute the command
for cmd in command:
    subprocess.run(cmd)