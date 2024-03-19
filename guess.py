import random
x=random.randint(10,50)
guess=0
while(guess != x):
    guess=int(input("enter a number"))
    if(guess>x):
        print("too high")
    else:
        print("too low")

print("congratulations")