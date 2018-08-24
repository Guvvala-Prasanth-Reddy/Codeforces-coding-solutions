a,l=input(),[]
for item in a:
    if(item.isalpha()):
        l.append(item)
print(len(set(l)))  