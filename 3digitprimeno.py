l=int(input("enter lower range"))
u=int(input("enter upper range"))

print("the prime numbers in range :")
for num in range(l,u+1):
 if(num>1):
  
  for i in range (2,num-1):
    if(num % i ==0):
      break
  else:
      print(num)