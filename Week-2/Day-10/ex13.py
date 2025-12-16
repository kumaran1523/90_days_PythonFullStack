# Delete a file safely

import os

file_name="Stud/stud.txt"
if os.path.exists(file_name) and os.path.isfile(file_name):
    os.remove(file_name)
    print("File deleted successfully")
else:
    print("File not found ")