
num1=float(input("enter first number"))
num2=float(input("enter second number"))
op=input("enter any operator")
result=0
if(op=='+'):
    result=num1+num2
elif(op=='-'):
    if(num2>num1):
        result=num2-num1
    else:
        result=num1-num2
elif(op=='*'):
    result=num1*num2
elif(op=='/'):
    if(num2==0):
        print("no division can occur")
    else:
        result=num1/num2
else:
    print("input correct operator")
print("the result is",result)
    
    