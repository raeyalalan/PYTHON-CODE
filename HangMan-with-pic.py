def hangman(w):
    if(w==5):
        print("""
---------
        |
        |
        |
        |
        |
        |         
""")
    
    if(w == 4):
        print("""
------- __
       |__|
         |  
         |  
         |
         | 
         | 
""")

    if(w == 3):        
        print("""
------- __
      _|__|
     |   |  
     |   |  
         |
         | 
         | 
""")
        
    if(w == 2):
        print("""
------- __
      _|__|_
     |   |  |
     |   |  |
         |
         | 
         | 
""")
    if(w==1):
        print("""
------- __
      _|__|_
     |   |  |
     |   |  |
        _|
       | | 
       | | 
""")
    if(w==0):
        print("""
---------
        __
      _|__|_
     |   |  |
     |   |  |
        _|_
       | | |
       | | |
""")
        print("GAME OVER \n ****************************************************")








print("Welcome to The Hnagman Game!")
print("**************")
import random

#Variables and lists

tries = 6
word_list=["Know","Ready","Mother","Dolphin","Happy","Battery","Table","Octopus","Lion","Random"]
correct = []
word = random.choice(word_list)
word = word.upper()
print(word)

#While Loop

for i in range(len(word)):
    print(" _ ",end = " ")

while tries > 0:
    output = ''
    guess = input("\n Guess a letter: ")
    guess = guess.upper()
    if guess in word:
        print("Great Job! You guessed the correct letter!")
        correct.append(guess)
    else:
        print("Oops! Wrong letter guessed! \n")
        tries = tries - 1
        hangman(tries)
        
    for letter in word:
        if letter in correct:
            output = output + letter
        else:
            output = output + ' _ '
    if output==word:
        print("Congratulations! You have Guessed the word",output,"!")
        break
    print(output)
    print(tries,"tries left!")

if tries==0 and output==word:
    print("Hurray, You win! The word is",word)
elif tries==0 and output!=word:
    print("Oops!The game is over! The word is",word)
