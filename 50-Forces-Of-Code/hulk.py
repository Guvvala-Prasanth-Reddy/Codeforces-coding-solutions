a=int(input())
for i in range(a):
	print("I",end=" ")
	print(["hate","love"][i%2!=0],end=" ")
	print(["that ","it"][i==a-1],end="")	