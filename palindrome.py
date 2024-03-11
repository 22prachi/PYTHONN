num=int(input("enter a number"))
n=num
rev=0
while(num != 0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
     
if (n==rev):
    print("it is palindrome number")
else:
    print("it is not palindrome")

