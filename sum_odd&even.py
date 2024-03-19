n=int(input("enter upto which natural numbers"))
sumEven=0
sumOdd=0
for i in range(1,n):
    if(i % 2 == 0):
        sumEven+=i
    else:
        sumOdd+=i

print("sum of odd numbers",sumOdd)
print("sum of even numbers",sumEven)
