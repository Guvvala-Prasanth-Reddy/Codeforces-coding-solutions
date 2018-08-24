a=int(input())
l,m,f=[],[],0
for i in range(a):
	b,c =map(int,input().split())
	l.append(b),m.append(c)
for item in m:
	f+=l.count(item)
print(f)	