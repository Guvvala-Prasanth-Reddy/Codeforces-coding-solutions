import math
a=int(input())
k=list(map(int,input().split()))
l=[]
for item in k:
	if(item>0):
		if(math.sqrt(item)%1!=0):
			l.append(item)
	elif(item<0):
		l.append(item)        
l.sort()
print(l[-1])		
		
