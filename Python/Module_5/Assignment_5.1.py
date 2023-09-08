"""
5. List structures and iterative loops (for)

    5.1. Write a program that asks the user how many dice to roll. The program
         rolls all the dice once and prints out the sum of the numbers. Use a
         for loop.

"""
from random import randint

dice_nums = []
nums = int(input('How many dice do you want to roll?\n'))
for item in range(nums):
    dice_nums.append(randint(1, 6))

amount = sum(dice_nums)

print(f'The amount of the dice is {amount}') 
