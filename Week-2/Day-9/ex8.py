# Use os module to check file exists

import os

if os.path.exists("Stud.txt"):
    print('The file is exist')
else:
    print('The file is not exist')
    