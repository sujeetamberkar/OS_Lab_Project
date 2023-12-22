import os
import sys

def remfile(file_name):    
    if(os.path.exists(file_name)) :
        if(os.path.isfile(file_name)):
            os.remove(file_name)
            print("File removed successfully!\n")
        else :
            print("Error: Not a file!")
    else :
        print("File doesn't exist")

remfile(sys.argv[1])
