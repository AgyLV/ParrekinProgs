import subprocess
import os

#print('File name :    ', os.path.basename(__file__))
a=os.path.dirname(__file__)

# Path to DOSBox executable
dosbox_path = r"C:\Program Files (x86)\DOSBox-0.74-3\DOSBox.exe"  # Update this to your DOSBox path

# Commands to execute inside DOSBox
commands = [
    "mount c " + a,
    "c:",
    "Riga_TR.exe Riga_TR.txt Riga_O.txt",
    #"exit"  # To close DOSBox after running commands
]

# Construct the argument list
args = [dosbox_path]
for cmd in commands:
    args.extend(["-c", cmd])

# Run DOSBox with the commands
subprocess.run(args)