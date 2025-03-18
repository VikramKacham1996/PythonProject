import os

print(os.getcwd())
#return the current working directory


#list files in the current directory
files = os.listdir('/Users/vikky/PycharmProjects/PythonProject')
print(f"Files in current directory:{files}")

# create a new directory
os.mkdir ('Test31 for Lab170') # it will create a new directory  and same  of directory we can't create

#check if a file exists
file_exist = os.path.exists("TestData1.txt")
print(file_exist)

print(os.name) #posix == mac and window == nt