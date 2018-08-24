a=int(input())
l=[5,4,3,2,1]
f,i=0,0
while(a>0):
	f+=a//l[i]
	a=a%l[i]
	i=i+1
print(f)