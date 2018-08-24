a=int(input())
b=list(map(int,input().split()))
k=[None]*len(b)
for item in b:
	a=b.index(item)
	k[item-1]=str(a+1)
print(" ".join(k))	