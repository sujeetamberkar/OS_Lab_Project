import psutil
import sys
def memory():
    print("RAM usage in % : ",psutil.virtual_memory()[2])
    print("Total memory : ",round(psutil.virtual_memory()[0]/1000000000,3),"GB")
    print("Available memory : ",round(psutil.virtual_memory()[1]/1000000000,3),"GB")
memory()
