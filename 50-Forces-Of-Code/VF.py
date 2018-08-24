a,b=map(int,input().split())
c=list(map(int,input().split()))
f=0
for item in c:
	if(item>b):
		f+=1
print((a+f))