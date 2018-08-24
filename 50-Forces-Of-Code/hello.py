import sys
a=input()
a=a.lower()
a=list(a)
k="hello"
k=list(k)
f=[]
m=0
for i  in range(len(k)) :
	if k[i] in a:
		f.append(a.index(a[i]))
		for j in range(a.index(a[i])):
			a[j]='1'
		a[a.index(a[i])]='1'
m=0
for i in range(len(f)-1):
	if(f[i]<f[i+1]):
		m=m+1
if(m==len(f)-1):
	print("Yes")
else:
	print("No")

