import sys
import random
from enum import Enum # notice the different capitalization

print("")

class RPS(Enum):
    ROCK = 1
    SCISSORS = 2
    PAPER = 3

playagain = True

while playagain:

    print("")
    playerchoice = input("Enter... \n1 for Rock, \n2 for Scissors, or \n3 for Paper:\n\n") # n\ represents a new lin
    player = int(playerchoice) # must change data type to integer 

    if player < 1 or player > 3: 
        print("\nYou must enter 1, 2, or 3.")
        continue
    computerchoice = random.choice("123")
    computer = int(computerchoice)
    2
    print("") 
    print("You chose " + str(RPS(player)).replace('RPS.','') + ".") # RPS to replace values with string (name of object chosen) and replace function to get rid of RPS
    print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".")
    print("")

    if player == 1 and computer == 2:
        print("You win!")
    elif player == 2 and computer == 3:
        print("You win!")
    elif player == 3 and computer == 1:
        print("You win!")
    elif player == computer:
        print("Tie game!")
    else:
        print("Python wins hahahahahha!")

    playagain = input("\nPlay again? \ny for yes or \nn for no \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\nThanks for playing!")
        playagain = False 

