sum=0
ans="y"
while (ans=="y"):
   
    x=int(input("enter a number"))
    if(x<0):
        print("number is less than zero")
        break
    sum+=x
    ans=input("enter yes or no")

print("sum too far is",sum)