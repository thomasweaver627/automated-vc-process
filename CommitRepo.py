import os
from pathlib import Path
# retrieves filepath info 
import subprocess
# to interact with shell
from datetime import datetime

# combine add/commit into one EXE?


fileName = ""
# get user input here? user could specify file if they only want to add/commit a single file

subprocess.run(['git', 'add', '.'])

# will either use a cmd prompt or tkinter to get user input
commitMsg = input("Please enter a concise commit message for changes made: ")
dt = datetime.now().strftime("%Y%m%d-%H_%M_%S_%p")
commitOutput = f"{fileName}_commit_{dt}.txt"

subprocess.run(['git', 'commit', '-m', f'\"{commitMsg}\"', '>', commitOutput])
# commits changes and sends output to user for confirmation before pushing to repo

f = open(commitOutput)
# validate 
f.close()

# after user validates the commit, still deciding between two options:
# 1. prompt for user to validate output before continuing script
# 2. end script and use separate script for pushing changes