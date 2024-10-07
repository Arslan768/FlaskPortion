import subprocess
import os

def run_rhubarb(input_file, dialog_file, output_file, recognizer='phonetic', export_format='json', quiet=False):
    # Change to the desired directory
    exe_dir = r'C:\Users\pc\Desktop\AvatarLipSyncReact\rhubarb_main'

    os.chdir(exe_dir)

    # Construct the command
    command = ['rhubarb.exe']
    
    # Add options based on parameters
    # command.append('-r')
    # command.append(recognizer)
    
    command.append('-f')
    command.append(export_format)
    
    if quiet:
        command.append('-q')
    
    command.append('-d')
    command.append(dialog_file)
    
    command.append('-o')
    command.append(output_file)
    
    command.append(input_file)  # The input file is always the last argument
    
    try:
        # Run the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Print the output and errors if any
        print("Output:", result.stdout)
        print("Errors:", result.stderr)
    
    except subprocess.CalledProcessError as e:
        print("An error occurred while running rhubarb.exe:")
        print("Return code:", e.returncode)
        print("Output:", e.stdout)
        print("Errors:", e.stderr)

