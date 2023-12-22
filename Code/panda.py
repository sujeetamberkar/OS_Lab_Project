import sys
import os
from os import system
import time
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

t =sys.argv[1]
  
# function call
countdown(int(t))
