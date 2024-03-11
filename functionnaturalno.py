def sum():
    sum=0
    n=int(input("enter number upto which u need a sum"))
    for i in range(1,n+1):
        sum=sum+i
    print("the sum of",n,"natural numbers is",sum)

sum()
