k,n=map(int,input().split())
l=sorted(list(map(int,input().split())))
l.reverse()
g=[]
for i in range(n-k+1):
	g.append(l[i]-l[i+k-1])
print(min(g))