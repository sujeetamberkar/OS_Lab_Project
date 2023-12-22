import os
import sys
def list():
    for filename in os.listdir('.'):
        print(filename,"\t")
def listpath(path):
    for filename in os.listdir(path):
        print(filename,"\t")
        
if(len(sys.argv)==1):
    list()
elif(len(sys.argv)==2):
    listpath(sys.argv[1]) 
         

