# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

hidden = random.randrange(1, 201)
print(hidden)
guess = int(input("Please enter your guess: "))
 
if guess == hidden:
    print("Hit!")
elif guess < hidden:
    print("Your guess is too low")
else:
    print("Your guess is too high")

    