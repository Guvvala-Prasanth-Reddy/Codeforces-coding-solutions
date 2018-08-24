a=list(map(int,input().split("+")))
a.sort()
k=[]
for i in range(len(a)):
	if(i!=len(a)-1):
		print(str(a[i]),"+", end="")
	else:
	    print(str(a[i]), end="")	    	    	