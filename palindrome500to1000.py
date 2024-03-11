i=500
while(i<1000):
    
    rev=0
    n=i
    while(i>0):
     rem=i%10
     rev=rev*10+rem
     i=i//10
     
    if(n==rev):
      print(n)
    i=i+1