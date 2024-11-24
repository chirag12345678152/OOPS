# write a python programm capable of playing this game with the user
import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = -1
computer = random.choice([1,0,-1])
youstr = input("enter your choice: ")
youdict = {"s":1, "w":-1, "g":0}
you = youdict[youstr]
reversedict = {1 : "snake", -1 : "water", 0 : "gun"}

print(f"you choose {reversedict[you]}\n computer choose {reversedict[computer]}")
 
if(you == computer):
    print("it is draw")
else:
    if(computer==-1 and you==1):
        print("you win!")
    elif(computer==-1 and you==0):
        print("you lose!")    
    elif(computer==1 and you==-1):
        print("you lose!")         
    elif(computer==1 and you==0):
        print("you win!") 
    elif(computer==0 and you==-1):
        print("you win!")   
    elif(computer==0 and you==1):
        print("you lose!")  
    else:
        print("something went wrong")             
