a=int(input())
a1=0
b1=0
l=0
for i in range(a):
	m,n=map(int,input().split())
	if(m+n-a1 > l): 
		l=m+n-a1
	a1=m 
	b1=n
print(l)		

