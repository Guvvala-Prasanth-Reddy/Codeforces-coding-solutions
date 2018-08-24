q=[int(input()) for x in range(5)]
d=q.pop()
print(q)
print(d)
a=[0]*(d+1)
print(a)
for x in q:	
    a[::x]=[1]*len(a[::x])
    print(len(a))
    print(a)
print(a)    
print(sum(a)-1)