import os
import sys

def makedir(directory, dir_name):
    path = os.path.join(directory,dir_name)
    os.mkdir(path)
    print("Directory created successfully!\n")

makedir(sys.argv[1], sys.argv[2])