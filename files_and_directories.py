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

# path = Path()   # Define path to the current directory
# print(Path(__file__))
# # print(path.glob('*.py'))
#
# # for file in path.glob('*.py'):
# #     print(file)
#     # Here, this for loop prints all the .py file names in my current directory
#
# path1 = Path("test.py")
# path2 = Path('Test File')
# print(type(path1))
# print(type(path2))
# print(path1.exists())
# # path1.touch()   # Create the file test.py. Notice mkdir() creates a directory (folder), not a file
#
# # Create a file inside a folder
# # path2.mkdir()
# new_file = path2 / 'Test.py' # Define a new Path class object called new_file ("Test.py") within the directory defined by path2 ("Test File")
# print(type(new_file))
# # new_file.touch()
#
# template = '''
# # This is a test.
# import datetime
# print(f'Today is {datetime.date.today()}.')
# '''
#
# print(type(template))
#
# new_file.write_text('print("Hello world")') # Creates the Path object new_file as a file and write 'print("Hello World")' inside it.
# path1.write_text(template)  # Write template in object (file) path1, let the num in template be 2


# Create multiple files
# for item in range(1, 6):
#     file = Path(f'File_{item}.py')
#     file.write_text(template)

# Read the codes in a file
# content = new_file.read_text()
# print(content)


# Read files in a given directory (glob() method also works). glob('**/*') also shows the nested files and folders in the directory.
# Path('.').resolve()  # Print the directory of current folder
current_folder = Path('.')
# for path in current_folder.glob('**/*'):
#     # print(path.name)
#     print(path)


# # Delete all files in a particular type in directory
# for path in current_folder.glob('*.py'):
#     if 'test' in path.name.lower():
#         path.unlink()
#
#
# # # Delete a particular file/folder in current directory
# # path1 = Path('Test File')
# # Path(path1 / 'Test.py').unlink()    # Delete the file Test.py in Test File folder
# # Path('Test File').rmdir()   # Remove the folder Test File. You have to make sure folder is empty
#
# base_dir = Path(__file__).parent
# print(base_dir) # Print the parent folder of current file
# blog_folder = base_dir / 'website' / 'blog' # Define blog_folder object representing the folder blog in side current_folder / website
# blog_folder.mkdir(parents=True, exist_ok=True) # parents=True is needed to make Python automatically creates any uncreated parent folders in blog_folder
#                                                # exist_ok=True allow the blog_folder to be created again even if it already exists



# file = Path('Myfile.txt')
# file.touch()
# file.rename('myfile.txt')


## Path attributes
file = Path('myfile.txt')
# print(*dir(Path()), sep='\n')   # Print all methods and attributes of Path
file_name = file.name
file_suffix = file.suffix
file_stem = file.stem
file_create_datetime = file.stat().st_ctime

print(f'file_name: {file_name}')
print(f'file_suffix: {file_suffix}')
print(f'file_stem: {file_stem}')
print(f'file_create_datetime: {file_create_datetime}')





