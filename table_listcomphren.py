n=int(input("enter a number"))
num=int(input("enter upto where"))
list=[f"{n} * {i} ={n*i}" for i in range(1,num+1)]
print("\n".join(list))