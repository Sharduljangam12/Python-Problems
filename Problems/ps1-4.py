#using os module list all the files and directories in the specific path
import os

#Specify the directory you want to list
directory_path = '/New folder'

#List all the files and directories in the specified path
contents = os.listdir(directory_path)

#print each file and directly name
for item in contents:
    print(item)