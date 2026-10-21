options = ["ROCK", "PAPER", "SCISSORS"]
c_points = 0
u_points = 0
import random

while c_points < 6 or u_points < 6:
    uchoice = input("Type Rock/Paper/Scissors or Q to Quit. ").upper()
    if uchoice == "Q":
        break
    print("Computer's Chance: ")
    chance = random.randint(0,2)
    #Rock = 0, Paper = 1, Scissors = 2
    computer_pick = options[chance].upper()
    print("\n Computer chose",computer_pick)
    if computer_pick == uchoice:
        print("TIE")
        
    elif computer_pick == "ROCK" and uchoice == "PAPER":
        print("You won this Round!")
        u_points += 1
        
    elif computer_pick == "PAPER" and uchoice == "SCISSORS":
        print("You won this Round!")
        u_points += 1
    elif computer_pick == "SCISSORS" and uchoice == "ROCK":
        print("You won this Round!")
        u_points += 1
    else:
        print("The computer Wins this Round!")
        c_points += 1
    if u_points == 5:
        print("You win the game!")
        break
    elif c_points == 5:
        print("The computer wins this game!")
        break
    print("Your score is",u_points)
    print("The computer's score is",c_points)
        
        








