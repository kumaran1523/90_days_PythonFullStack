# List all files in current directory

import os

file=os.listdir()

for i in file:
    print(i,end=", ")