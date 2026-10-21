import os
import time

snakesandladders = {1:38, 4:14, 9:31, 21:42, 28:84, 51:67, 54:34, 62:19, 64:60, 72:91, 80:99, 87:36, 93:73, 95:75, 98:79}

def snakeorladder(name, position, snakeladder = {}):
    previous_position = position
    newposition = snakeladder.get(position, position)
    if previous_position > newposition:
        print("You were bitten!")
        #print("Position of ", name, ": ", newposition)
        return newposition
    elif previous_position < newposition:
        print("You climbed a ladder!")
        #print("Position of ", name, ": ", newposition)
        return newposition
    elif previous_position < 101 and newposition < 101:
        #print("Position of ", name, ": ", newposition)
        return newposition

import random
def roll():
    dice = random.randint(1,10000) 
    dice = dice % 6
    if dice == 0:
        dice = 6
    return dice

def chance(position):
    dice = roll()
    if dice == 6 and  dice + position < 100:
        print("You rolled ", dice, "Press 'k' to roll again!")
        c = input()
        if c == "k":
            return dice + roll()
    elif dice == 6 and dice + position > 100:
        print("You rolled ", dice, "Press 'k' to roll again!")
        c = input()
        if c == "k":
            return roll()
    else: 
        return dice
    
def player(name, position):
        print("\n", name, ": Press 'k' to roll")
        c = input()
        if c == "k":
            rolled = chance(position)
            print("You rolled ", rolled)

        if rolled + position < 101:
            position = position + rolled
            position = snakeorladder(name, position, snakesandladders)
            return position

        elif rolled + position > 100:
            print("Position remains at: ", position)
            return position

print("Enter the number of players: ", end = "")
e = int(input())
names = []
positions = []

for i in range(e):
    print("Player ", i+1, "enter your name: ", end = "")
    c = input()
    names.append(c)
    positions.append(0)

while positions[i] < 100:
    time.sleep(1)
    os.system('cls')
    for i in range(len(names)):
        positions[i] = player(names[i], positions[i])
        
        for j in range (len(names)):
            print("Position of ", names[j], "is: ", positions[j])
        
        if positions[i] == 100:
            print(names[i], " Wins !")
            break
