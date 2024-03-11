import random
def guess(x):
    
    random_no=random.randint(1,x)
    
    guess=0
    while(guess != random_no):
         guess=int(input(f"guess number between 1 to {x}="))
         if(guess<random_no):
              print("sorry,guess again. Too low ")
         elif(guess>random_no):
              print("sorry,guess again. Too high ")
 
    print("yay,u have guessed the number")

def comp_guess(x):
     low=1
     high=x
     feedback=''
     while(feedback!='c'):
          if(low != high):
             guess=random.randint(low,high)
          else:
               guess=low  #could be guess=high bcz high =low
          feedback=(input(f"is {guess} too high(h) or too low(l) or correct(c) ?"))
          if(feedback=='h'):
               high=guess-1
          elif(feedback=='l'):
               lowh=guess+1

     print("yay computer guessed the right number {guess}")

n=int(input("enter upper range of randint function"))
guess(n)
comp_guess(1000)