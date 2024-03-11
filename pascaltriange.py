
n=int(input("enter no of rows"))
for i in range(n):
   print(' '*(n-i),end=" ")
   print(' '.join(map(str,str(11**i))))




def tri(n):
 for i in range(0,5):
   for j in range(0,i):
      print(11**i)

print(tri(5))