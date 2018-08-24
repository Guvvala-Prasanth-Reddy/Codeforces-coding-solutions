a=int(input())
b1,l=0,0
for i in range(a):
	m,n=map(int,input().split())
	if(l<n+b1-m):
		l=n+b1-m
		print(l)
	b1=b1-m+n
print(l)		

