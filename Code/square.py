import sys
# Arguments passed

def square(arguments):
	arguments=int(arguments)
	arguments=arguments*arguments
	print(arguments)


square(sys.argv[1])
