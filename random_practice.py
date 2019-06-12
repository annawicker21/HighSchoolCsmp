"""
title: random_practice
author: Anna
date: 2019-06-12 09:53
"""

import random

name = input("Enter your name:")
salary = input("Enter your salary:")
salary = int(salary)

print(f"{name}, your current salary is {salary}")

raise_per = (random.randint(0, 100))

print(f"Your raise is {raise_per}% of ${salary}")

raise_amount = int((raise_per * salary * .01)+ salary)

print(f"{name}, your new salary is {raise_amount}")