f=0
k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
for j in range(d+1):
	if(j%k!=0 and (j%l!=0 and (j%m!=0 and j%n!=0)) and j > 0):
		f=f+1
print(d-f)