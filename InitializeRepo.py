import os
import subprocess
# allows a python script to interact with shell

# in progress...


# initializes a git repo in the current directory

workingDir = os.getcwd() 

subprocess.run(['git', 'init', workingDir])
