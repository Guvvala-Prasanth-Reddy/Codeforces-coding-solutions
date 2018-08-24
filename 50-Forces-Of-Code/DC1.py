a=int(input())
b=list(set(input().lower()))
print(["YES","No"][len(b)!=26])