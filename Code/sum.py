import sys 


def function():
	n=len(sys.argv)
	sum=0
	for i in range(1,n):
		temp=sys.argv[i]
		sum=int(temp)+sum

	print(sum)

function()