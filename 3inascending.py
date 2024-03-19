x=int(input("enter a first number"))
y=int(input("enter a second number"))
z=int(input("enter a third number"))
min=mid=max=None
if(x != y and y != z and x!=z):
 if(x<y and x<z):
    if(y<z):
        min,mid,max=x,y,z
    else:
        min,mid,max=x,z,y
 if(y<z and y<x):
    if(x<z):
        min,mid,max=y,x,z
    else:
        min,mid,max=y,z,x
 if(z<x and z<y):
    if(x<y):
        min,mid,max=z,x,y
    else:
        min,mid,max=x,y,z
 print("numbers in ascending order",min,mid,max)
else:
   print("duplicate numbers")

