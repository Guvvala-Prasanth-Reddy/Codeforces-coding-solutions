a,i,l,p=list(input()),0,'hello',0
for item in l:
	if(a.index(item)>=i):
		p+=1
		i=a.index(item)
		a[i]='0'
		print(a)
print(["NO","YES"][p==5])				