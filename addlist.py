list1=eval(input("Enter a list to be added"))
print("list you entered",list1)
length=len(list1)
sum=0
for i in range(0,length):
    sum=sum+list1[i]
print("sum of all items of nummeric list",sum)