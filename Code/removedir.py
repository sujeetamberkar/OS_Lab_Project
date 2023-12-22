import os
import sys

def remdir(dir_name):    
    if(os.path.exists(dir_name)) :
        if(os.path.isdir(dir_name)) :
            os.rmdir(dir_name)
            print("Directory removed successfully!\n")
        else :
            print("Error: ",dir_name," is not a directory")
    else :
        print("Directory doesn't exist")
remdir(sys.argv[1])
