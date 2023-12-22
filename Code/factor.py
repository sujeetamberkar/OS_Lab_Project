import sys
# Arguments passed

def factors(arguments):
	arguments=int(arguments)
	for i in range(1,arguments + 1):
		if arguments % i == 0:
			print(i,end="")
			print(" ",end="")

			pass
factors(sys.argv[1])


