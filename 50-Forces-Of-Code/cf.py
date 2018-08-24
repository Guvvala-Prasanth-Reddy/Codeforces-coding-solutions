l=0
def fun(b,l):
	k=0
	for i in range(len(b)-1):
		if(b[i]==b[i+1]):
			b.pop(i)
			l=l+1
			return fun(b,l)
	return(l)	
a=int(input())
b=input()
b=list(b)
f=fun(b,l)
print(f) 	    	
