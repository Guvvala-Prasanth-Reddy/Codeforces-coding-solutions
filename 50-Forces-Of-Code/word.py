k,a=0,list(input())
for item in a:
	if(item.isupper()):
		k+=1
	else:
	    k-=1	
print(["".join(a).upper(),"".join(a).lower()][k<=0])