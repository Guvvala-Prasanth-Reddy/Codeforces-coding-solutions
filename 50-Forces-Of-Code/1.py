m,n=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
arr.reverse()
k=list(set(arr))
k.sort()
k=k[len(k)-n]
print(k)
f=0
print(arr)
for item in arr:
    if(item == k):
        break
    else:
        f+=1
print(f)    





