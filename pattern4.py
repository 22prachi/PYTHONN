for rows in range(1,4):
    for spaces in range(3,rows,-1):
        print(" ", end ="")
    for star in range(0,2*rows-1):
        print("*", end=" ")
    print()