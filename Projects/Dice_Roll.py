""" `
Author: Shayna Fu
Date: June 13, 2020
DICE ROLL!
"""
import random

print("Welcome to Dice Roll!")

def DiceRoll(dice1):
    for i in range(dice1):
        dice1 = random.randint(1, 6)
        print(">><<")
        print("*" + str(dice1) + "*")
        print(">><<")
        print()
    Options()    
    

def doubleRoll(dice2):
    for i in range(dice2):
        dice2 = random.randint(1, 12)
        print(">><<")
        print("*" + str(dice2) + "*")
        print(">><<")
        print()
    Options()


def Options():
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
        doubleRoll(1)
        if doubleRoll() % 2 == 0:
            print("fsdf")
        
    if choice == 3:
        exit();

Options()    
