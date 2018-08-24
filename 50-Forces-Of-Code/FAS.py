a,b=map(int,input().split())
for i in range(a):
	if(i%2==0):
		print(b*'#')
	elif((i//2)%2==0):
	    print('.'*(b-1)+'#')
	else:
	    print('#'+(b-1)*'.')    	