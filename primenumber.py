flag=True
num=int(input("Enter a number"))
for i in range(2,num-1):
    if(num%i == 0):
       flag=False
       break
    else:
        flag=True
        
if(flag==True):
    print("It is prime number")
else:
    print("it is Composite number")
   
