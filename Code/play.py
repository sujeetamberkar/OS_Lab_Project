from random import *
from os import system
commands=[
		 "aafire",
		 "sl",
		 "fortune"
		 ]

n=len(commands)
n=n-1
x = randint(0, n)
system(commands[x])
