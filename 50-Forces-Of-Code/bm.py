l=[]
for i in range(5):
	a=list(map(int,input().split()))
	l.append(a)
for i in range(5):
	f=l[i]
	if 1 in f:
		x,y=i,f.index(1)
		break
print(abs(x-2)+abs(y-2))			    