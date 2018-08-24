a=int(input())
b=list(map(int,input().split()))
l=b.index(max(b))
b.reverse()
k=b.index(min(b))
k=len(b)-k-1
print([l+len(b)-k-2,l+len(b)-k-1][l<=k])