import os
from pdb import find_first_executable_line

try:
    full_path = os.getcwd()
    print(full_path)
    full_path_file = full_path+ "/example.txt"
    print(full_path_file)

# read the file
    file =open(full_path_file) #FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\vikky\\PycharmProjects\\PythonProject\\Dec\\ex_07122024_Exceptions/example.txt'
except Exception as e:
     print("file not found, Fix the path or create a file")
finally:
    print("This code will be executed anyhow")