import os
import sys
def check(f,per):
    for fi in os.listdir(".") :
        if(fi==f) :
            if(os.path.isdir(f)) :
                print("Error: directory with same name already exists!")
            else :
                print("Error:File with the same name already exists")
            exit()  
check(sys.argv[1],sys.argv[2])
open(sys.argv[1],sys.argv[2])
os.system("gedit "+sys.argv[1])
