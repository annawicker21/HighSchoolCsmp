"""
title: loop_practice
author: Anna
date: 2019-06-13 13:38
"""

#1

for i in [89, 41, 73, 90]:
    print(i)

#2

for l in range(5, 16):
    print(l, end = " ")

#3

for x in range(100, 201, 10):
    print(x, end = " ")

#4

for num in range(80, 31, -8):
    print(num)

#5

for f in range(3):
    print("alright", end=" ")


#while loop 1
number = 10
while (number > 0):
    print(number, end = "-")
    number -= 1
    print("Countdown finished")

#while loop 2

num_input = int(input("Enter number greater than 0"))

while num_input <= 0:
    print("Not greater than 0")
    num_input = input("Enter number greater than 0")

print("True")

#while loop 3

first = int(input("Enter a number:"))
second = int(input("Enter a smaller number:"))

while second < first:
    second = int(input("Invalid response. Enter a second number: "))

while first < second:
    print(first)
    first += 1
    second = input("Enter number smaller than first")

print("true")


#while loop 4

x = input("Enter response ('Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO'): ")

while x not in ['Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO']:
    x = 