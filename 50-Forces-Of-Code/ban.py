k,n,w=map(int,input().split())
k=k*(w*(w+1)/2)-n
if(k>0):
	print(int(k))
else:
    print('0')	