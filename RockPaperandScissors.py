import random
def play():
    computer=random.choice(['r','p','s'])
    user=input("what's your choice ? 'r' for rock 's' for scissors 'p' for paper \n" )
    if(computer==user):
        return "it is tie"
    
    if is_win(computer,user):
      return ("you won and word is",computer)
    

    return ("you lost and word is",computer)


def is_win(opponent,player):
     if (opponent=="r" and player=="p") or( opponent=="s" and player=="r" )or (opponent=="p" and player=="s"):
        return True
     
print(play())