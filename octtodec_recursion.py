def octtodec(n,exp=1):
    if(n==0):
        return 0
    else:
        rem=n%10
        rem=rem*exp
        return rem+octtodec(n//10,exp*8)
    
n=int(input("enter octal number"))   
print(octtodec(n))
            