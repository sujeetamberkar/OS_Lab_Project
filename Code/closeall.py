import os
import sys
def removeall(path):
    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if os.path.isfile(f):
            os.remove(f)
        elif (os.path.isdir(f)) :
            removeall(f)
            os.rmdir(f)
if(os.path.isdir(sys.argv[1])):
    removeall(sys.argv[1])
    os.rmdir(sys.argv[1])
    print("Removed directory successfully")
else :
    print("Error: Not a directory!")
    
