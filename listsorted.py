def is_sorted():

 l1=eval(input("enter a list"))
 length=len(l1)
 for i in range(0,length-1):
   if(l1[i]>l1[i+1]):
      return False
 return True
  
print(is_sorted())