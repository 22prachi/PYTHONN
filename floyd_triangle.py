sum=1
n=int(input("enter no of rows"))
for rows in range(1,n):
    for column in range(1,rows):
      print(sum,end=" ")
      sum=sum+1
    print()