n,c=map(int,input().split())
k=list(input())
for i in range(c):
	j=0
	while(j<len(k)-1):
		if(k[j]=='B' and k[j+1]=='G'):
			l=k[j+1]
			k[j+1]='B'
			k[j]=l
			j=j+1
		j=j+1
print("".join(k))			
						

