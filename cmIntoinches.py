cm=float(input("enter a number in cm"))
ch=int(input("enter a choice"))
if (ch== 1):
    m=cm/100
    print("cm into m",m)
    
elif (ch== 2):
    inch=cm/2.54
    print("cm into inches",inch)

else:
    print("enter a right choice")