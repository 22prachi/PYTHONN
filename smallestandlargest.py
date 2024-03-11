l1=eval(input("enter a lsit to be entered"))
print("list you entered",l1)
Max=l1[0]
Min=l1[0]
for i in range(len(l1)):
   if(l1[i]>Max):
      Max=l1[i]
     
   elif(l1[i]<Min):
      Min=l1[i]
      
   
     
print("maximum in list is",Max)
print("minimum in list is",Min)