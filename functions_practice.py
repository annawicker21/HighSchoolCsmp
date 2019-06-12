"""
title: functions_practice
author: Anna
date: 2019-06-12 11:22
"""

def age_calculator (current_year, year_born):
    return int(current_year) - int(year_born)

current_year = input("Enter current year:")
year_born = input("Enter birth year:")
print(age_calculator(current_year, year_born))

def avg_numbers (x, y, z):
    return (int(x) + int(y) + int(z))/3

x = int(input("Enter X"))
y = int(input("Enter Y"))
z = int(input("Enter Z"))
print(avg_numbers(x, y, z,))