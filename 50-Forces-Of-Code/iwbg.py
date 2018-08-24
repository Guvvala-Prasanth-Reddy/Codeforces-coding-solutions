a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
b,c=b[1:],c[1:]
print(["Oh, my keyboard!","I become the guy."][len(list(set(list(set(b))+list(set(c)))))== a])