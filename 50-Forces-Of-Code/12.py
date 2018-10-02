n,k=map(int,input().split())
a=list(map(int,input().split()))
p=0
for i in range(len(a)):
    if(a[i]%k==0 and a[i]//k > p): # // is used for integer divison
        p=a[i]//k
        
print(p)        
