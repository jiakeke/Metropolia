"""
6. Functions

    6.2. Modify the function above so that it gets the number of sides on the
         dice as a parameter. With the modified function you can for example
         roll a 21-sided role-playing dice. The difference to the last exercise
         is that the dice rolling in the main program continues until the
         program gets the maximum number on the dice, which is asked from the
         user at the beginning.

"""

from random import randint


def roll_dice(max_sides):
    return randint(1, max_sides)


max_sides = int(input('Please input the max sides of the dice: '))

while True:
    result = roll_dice(max_sides)
    print(f'Rolling points is: {result}')
    if result == max_sides:
        break
