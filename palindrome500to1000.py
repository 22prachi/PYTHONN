def palin(num):
    return str(num)==str(num)[::-1]

for i in range(500,1001):
    if (palin(i)):
        print(i)