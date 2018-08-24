a,b=map(int,input().split())
x,y,k=[],[],0
for i in range(b):
	c,d=map(int,input().split())
	x.append(c)
	y.append(d)
for i in range(b):
	if(a>min(x)):
		a=a+y[x.index(min(x))]
		y.pop(x.index(min(x)))
		x.pop(x.index(min(x)))
	else:
		k+=1
print(["YES","NO"][k!=0])           	    	    	