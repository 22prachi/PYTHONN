def sum(a,r,n):
    sum=0
    i=0
    while(i<=n):
        sum=sum+a
        a=a*r
        i=i+1
    return sum

a=int(input("Enter the first term of geometeric series :"))
r=int(input("Enter common ratio :"))
n=int(input("Enter no of terms :"))
x=sum(a,r,n)
print("geometeric series upto",n,"terms is")
print(x)


def georecursion(a,r,n):
    if n==0:
        return 1
    else:
        return a*pow(r,n)+(georecursion(a,r,n-1))

a=int(input("Enter the first term of geometeric series :"))
r=int(input("Enter common ratio :"))
n=int(input("Enter no of terms :"))
x=georecursion(a,r,n)
print("geometeric series upto",n,"terms is")
print(x)
