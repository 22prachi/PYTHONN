n=int(input("enter no of rows"))
for rows in range(1,n):
    for spaces in range(0,4-rows):
        print(" ", end =" ")
    for star in range(0,2*rows-1):
        print("*", end=" ")
    print()