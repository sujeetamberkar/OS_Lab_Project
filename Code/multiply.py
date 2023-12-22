import sys 
def function():
	n=len(sys.argv)
	mul=1
	for i in range(1,n):
		temp=sys.argv[i]
		mul=int(temp)*mul

	print(mul)

function()