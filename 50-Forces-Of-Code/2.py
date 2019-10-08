t=int(input())
k=0
for i in range(t):
    k=0
    a=int(input())
    b=list(map(str,input().split(' ')))
    for j in range(len(b[a])):
        if(b[a][j].isalpha()):
            k+=ord(b[a][j]) # ord is function to get ascii value
    if(k>0):
        print(k)
    else:
        print(-1)
        
