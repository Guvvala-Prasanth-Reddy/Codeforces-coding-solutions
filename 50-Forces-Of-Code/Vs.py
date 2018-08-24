a,b=map(int,input().split())
mini,i=a,0
while(mini>0):
	mini=mini//b
	i+=1
print(a+i)	