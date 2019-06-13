"""
title: string_practice
author: Anna
date: 2019-06-11 13:45
"""

#strings lab

#answer = input("Enter a character:")
#character = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
#print(answer in character)

#short hand

#short_hand = input("Enter a phrase")
#new_short_hand = short_hand.replace("and", "&").replace("too", "2").replace("you", "U").replace("You", "U").replace("for", "4")\
#    .replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
#print(new_short_hand)

#Remove Case and Punctuation

def phrase(punctuation):
    punctuation = punctuation.lower().replace(",", "").replace("'", "").replace(" ", "")
    return punctuation

new_phrase= input("Enter phrase:")
print(phrase(new_phrase))

#Palindrome

palindrome = input("Enter phrase:")
palindrome = phrase(palindrome)
backwards = palindrome[::-1]
print(palindrome == backwards)