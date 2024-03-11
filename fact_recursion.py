def fact(n):
    if(n==0):
        return 1
    elif(n>0):
        return n*fact(n-1)
    else:
        return "doesnot exist"

n=int(input("enter a number"))
f=fact(n)
print("factorial of number ",f)
    
