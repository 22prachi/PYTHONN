def fibonaaci(n):
    if(n<=1):
        return n
    else:
        return fibonaaci(n-1)+fibonaaci(n-2)

nterms=int(input("how many terms required in series?"))  
print("fibonacci series generated is")
for i in range(0,nterms):
    print(fibonaaci(i))