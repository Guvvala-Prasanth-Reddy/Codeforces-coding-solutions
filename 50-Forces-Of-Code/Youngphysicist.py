a,b,c=0,0,0
for i in range(int(input())):
	m,n,o=map(int,input().split())
	a=a+m
	b=b+n
	c=c+o
if(a==0 and b==0 and c == 0 ):
    print("YES")
else:
    print("NO")    	
 