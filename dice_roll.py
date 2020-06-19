"""
Author: Shayna Fu
Date: June 15, 2020

DICE ROLL
"""

import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print(dice1)
print(dice2)
print("I rolled a",(dice1+dice2),"!")
if dice1 == dice2:
    print("I rolled a double!")
else:
    if dice1 == 1 and dice2 == 1:
        print("I rolled snake eyes!")


