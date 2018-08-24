a,b=int(input()),list(map(int,input().split()))
for i in range(len(b)):
	b[i]=b[i]%2
if(b.count(1)==1):
	print(b.index(1)+1)
else:
    print(b.index(0)+1)