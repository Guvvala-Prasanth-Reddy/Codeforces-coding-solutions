n,k=map(int,input().split())
a=list(map(int,input().split()))
p=0
for i in range(len(a)):
    if(a[i]%k==0 and a[i]//k > p):
        p=a[i]//kint
    else:
        print()
        
print(p)        
