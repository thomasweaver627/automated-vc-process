import os
# to access scandir function, which grabs each file in a directory 
from pathlib import Path
# to access Path function, which retrieves the paths of each directory item
import subprocess
# allows a python script to interact with shell

# In Progress...
# this script will either be located in a specified folder or any folder chosen by the user
# leaning toward a specified folder to encourage consistency 


try:

    # workingDir = os.getcwd() 
    repoDir = input("Please enter the full file path of repository: ")

    subprocess.run(['git','clone', repoDir])
        # run() is the current standard (when possible) for invoking the subprocesses module
        # https://docs.python.org/3.10/library/subprocess.html

except:
    print("Clone unsuccessful. Please check for typos, or confirm this path is an existing repository.")