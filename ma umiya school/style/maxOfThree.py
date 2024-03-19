x=int(input("enter a first number"))
y=int(input("enter a second number"))
z=int(input("enter a third number"))
max=x
if(max<y):
    max=y
if(max<z):
    max=z

print("maximum of three number is",max)