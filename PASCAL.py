n=int(input("Enter n = "))
def fact(s):
  fact=1
  for i in range(1,s+1):
    fact=fact*i
  return fact

p=0
for i in range(1,n+1):
    for spaces in range(0,n-i+1):
       print(" ",end=" ")
    for k in range(0,i):
       print(int(fact(p)/int(fact(k)*fact(p-k))),"  ", end="")
    p=p+1
    print()

       
