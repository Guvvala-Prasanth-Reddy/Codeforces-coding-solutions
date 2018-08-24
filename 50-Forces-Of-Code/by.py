k=int(input())+1
while(k):
	if(len(set(str(k)))==len(str(k))):
		print(k)
		break
	k+=1	