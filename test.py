import subprocess

# Variables
testScript = './Image_Process_Scripts/convert.py';
inputDir = "./Input"
outputDir = "R:/Output"
formats = ["PNG", "BMP",  "GIF",  "TIFF", "WEBP", "PDF"]
inputImage = inputDir+"/FX_08_VirtualDrummerSolid.png";

# Define the command to be executed
command = []
# command.append(['python', './Image_Process_Scripts/contrast.py', inputImage ,"0.7","./Output/Test_autobalance_file.png"])
for fmt in formats:
    # command.append(['python', testScript , inputImage ,fmt,"./Output/Test_"+fmt.lower()+"_file."+fmt.lower()])
    command.append(['python', testScript , inputDir ,fmt,outputDir+"/Test_"+fmt.lower()+"_file."+fmt.lower()])


# Execute the command
for cmd in command:
    subprocess.run(cmd)