num=int(input("enter a number"))
sum=0
n=num
while(num!=0):
    rem=num%10
    sum=sum+rem*rem*rem
    num=num//10

if(n==sum):
    print("it is armstrong number")
  
else:
    print("it is not armstrong number")
  