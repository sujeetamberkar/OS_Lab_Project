import sys
import psutil
print("PID\t\tNAME")
for proc in psutil.process_iter():
    PName=proc.name()
    PID=proc.pid
    print(PID,"\t\t",PName)
