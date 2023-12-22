from random import *
from os import system
cd=[
	"I invented a new word! Plagiarism!",
   	"How does the ocean say hi? It waves!",
   	"What do birds give out on Halloween? Tweets.",
   	"What has ears but cannot hear? A cornfield.",
   	"What do you call a guy who’s really loud? Mike.",
   	"What’s Thanos’ favorite app on his phone? Snapchat.",
   	"Why was 6 afraid of 7? Because 7,8,9.",
   	"Which planet loves to sing? Nep-tune!"
   ]

n=len(cd)
n=n-1
x = randint(1, n)

temp=cd[x]
system('figlet -f slant '+temp)

