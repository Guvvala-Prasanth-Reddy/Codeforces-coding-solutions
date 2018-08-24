a,b=map(int,input().split())
if(b>a//2+a%2):
    print(2+(b-(a//2+a%2)-1)*2)
else:
    print(1+(b-1)*2)    	