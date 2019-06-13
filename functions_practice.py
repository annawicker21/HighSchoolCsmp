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


def is_letter(character):
    return character[0].lower() in "qwertyuiopasdfghjklzxcvbnm"

print(is_letter("i"))
print(is_letter("0"))

def short_hand(short):
    short = short.lower().replace("and", "&").replace("too", "2").replace("you", "U").replace("for", "4")
    short = short.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
    return short

phrase = input("Enter phrase:") #then enter "phrase" instead of phrase)
print(short_hand("Thank you for that! You are too sweet and kind"))
print(short_hand("How are you today?"))