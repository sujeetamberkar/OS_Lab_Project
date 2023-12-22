import os
import sys

def rnm(old_nm, new_nm):
    os.rename(old_nm,new_nm);
    print("Rename successful!\n")

rnm(sys.argv[1], sys.argv[2])