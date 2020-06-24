""" 
Author: Shayna Fu
Date: June 13, 2020
DICE ROLL!

INPUT 1 TO ROLL ONE DICE
INPUT 2 TO ROLL TWO DICE

"""
import random

print("(((((Welcome to Dice Roll!)))))")
print("(((((((5 Tokens To Play)))))))")

def DiceRoll(dice1):
    for i in range(dice1):
        dice1 = random.randint(1, 6)
        print(">><<")
        print("*" + str(dice1) + "*")
        print(">><<")
        if dice1 % 2 != 0:
            print("You rolled an odd number. You win!")
        else:
            print("You Lose. Try Again.")
        
    Options()    
    

def doubleRoll(dice2):
    for i in range(dice2):
        dice2 = random.randint(1, 12)
        print(">><<")
        print("*" + str(dice2) + "*")
        print(">><<")
        if dice2 % 2 == 0:
            print("You rolled an even number. You win!")
        else:
            print("You lose. Try Again.")
    Options()


def Options():
    print()
    print("RULES:")
    print("************************************************")
    print("Players must roll odd number with 1 dice to win!")
    print("************************************************")
    print("Players must roll even number with 2 dice to win!")
    print("---------------------")
    print("1. Roll One Dice")
    print("2. Roll Two Dice")
    print("3. Exit Game")
    print("---------------------")
    print()
    choice = int(input("I choose: "))
    print("Good Luck!")
    

    if choice == 1:
        DiceRoll(1)
        
    if choice == 2:
        dice2 = int(input("--ROLL TWICE FOR ALL OR NOTHING FOR 2 TOKENS-- How many times would you like to roll?: "))
        doubleRoll(dice2)
        
    if choice == 3:
        print("Are you sure you want to exit game?")
        exit();

Options()



    
