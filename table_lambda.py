x=int(input("enter a number"))
i=int(input("enter upto where"))
list=map(lambda i:f"{x}*{i}={x*i}",range(1,i+1))
print("\n".join(list))