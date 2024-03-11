def binarytodec(n,exp=1):
    if(n==0):
        return 0
    else:
        rem=n%10
        sum=rem*exp
        return sum+binarytodec(n//10,exp*2)
n=int(input("enter binary number"))   
print(binarytodec(n))
        