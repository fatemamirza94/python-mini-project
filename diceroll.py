# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

min = 1
max = 6

roll_again = 'y'

while roll_again is 'y':
    print("Rolling the dices ...")
    print("The values are ...")
    print(random.randint(min,max))
    print(random.randint(min,max))
    roll_again = input("Roll the dices again?")
    