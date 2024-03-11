n=int(input("enter a  number"))
for i in range(1,n):
    
    for j in range(1,n+1-i):
        print(" ",end=" ")
        
    for x in range(0,i):
        print("*",end=" ")

    
    print("\n")
