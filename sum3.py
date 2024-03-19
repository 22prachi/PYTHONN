x=int(input("enter a first number"))
y=int(input("enter a second number"))
z=int(input("enter a third number"))
sum1=x+y+z
sum2=0
if(x==y):
    if(z != x):
        sum2+=z
elif(y==z): 
    if(x != y):
        sum2+=x

elif(x==z):
        if(x != y):
           sum2+=y
else:
     sum2=x+y+z
    

print("sum 1",sum1)
print("sum2",sum2)