a=input()
if(a[0].isupper() and a[1:].isupper() and len(a)>1):
	a=a.lower()
elif(a[0].islower() and a[1:].isupper() and len(a)>1):
    a=a[0].upper()+a[1:].lower()
elif(len(a)==1):
    if(a.isupper()):
        a=a.lower()
    else:
        a=a.upper()        
print(a)