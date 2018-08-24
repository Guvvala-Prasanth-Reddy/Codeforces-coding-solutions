def gcd(n,m):
	if(n==0):
		return m
	else:
	    return gcd(m%n,n)
a,b,c=map(int,input().split())
k=0
while(c>0):
	if(k%2==0):
		c-=gcd(a,c)
	else:
	    c-=gcd(b,c)	
	k+=1
print(['0','1'][k%2==0])
