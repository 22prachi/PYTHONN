num=int(input("enter a number"))
sum=0
while(num!=0):
    rem=num%10
    sum=sum+rem
    num=num//10
print("sum of digits of n digit number",sum)