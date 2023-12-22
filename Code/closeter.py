from os import system
system('ps > temp.txt')


filepath = 'temp.txt'

with open(filepath) as fp:
   line = fp.readline()
   line = fp.readline()
   ctr=0
   ch=line[ctr]
   while ch==' ' :
      ctr=ctr+1
      ch=line[ctr]
   string=""
   while ch!=' ':
   	string=str(string)+str(ch)
   	ctr=ctr+1
   	ch=line[ctr]
   	
   string2="kill -9 "+string
   system(string2)
