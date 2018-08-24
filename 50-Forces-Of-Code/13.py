import time as t
a=t.time()
for i in range(10):
	print("Hello")
b=t.time()-a
print(str(b)+"is the execution time")	
