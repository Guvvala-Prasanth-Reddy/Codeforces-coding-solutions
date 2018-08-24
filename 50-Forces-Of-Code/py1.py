a=input()
a=a.lower()
a=list(a)
k=""
f=[]
l=[r'a',r'e',r'i',r'o',r'u']
for item in a:
	if item in l:
		a.remove(item)
print("."+(".".join(a)))
