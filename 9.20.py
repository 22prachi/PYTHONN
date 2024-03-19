for i in range(15,26):
    for x in range(2,i):
        if(i%x)==0:
            print(i,"is not prime number")
            break
    else:
            print(i,"is prime number")
