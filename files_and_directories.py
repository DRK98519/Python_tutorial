## Files and Directories
from pathlib import Path

# path = Path("email")
# path.mkdir()    # In the current folder, make a folder called email
# print(path.exists())
# path.rmdir()    # In the current folder, remove the folder called email
# print(path.exists())    # In the current folder, check if the folder called email exists. Returns boolean


# print(path.glob('*'))  # Search all files and all directories in the current path
# print(path.glob('*.*')) # Search only all files in the current path
# print(path.glob('*.py'))    # Search all .py files in the current path

path = Path()   # Define path to the current directory
# print(path.glob('*.py'))

for file in path.glob('*.py'):
    print(file)
    # Here, this for loop prints all the .py file names in my current directory



