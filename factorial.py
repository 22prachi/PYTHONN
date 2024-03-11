num=int(input("enter any number"))
fact=1
# i=1
# while(i<=num):
#     fact=fact*i
#     i+=1
for i in range(1,num+1):
    fact=fact*i
print("factorial of number is",fact)