k=input
a,b,c=list(k()),list(k()),list(k())
a=a+b
a.sort()
c.sort()
print(["NO","YES"]["".join(a)=="".join(c)])	
