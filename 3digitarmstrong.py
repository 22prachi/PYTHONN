l=int(input("enter lower range"))
u=int(input("enter upper range"))
print("all armstrong numbers in given range")
for num in range(l,u+1):
  order=len(str(num))
  sum=0
  n=num
  while(num!=0):
    rem=num%10
    sum=sum+rem**order
    num=num//10

  if(n==sum):
       print(n)
  
  else:
      continue
  