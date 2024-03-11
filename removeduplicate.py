l1=[2,3,4,4,1,5]
res=[]
for x in l1:
    if x not in res:
        res.append(x)
print("list without duplicates is",res)
