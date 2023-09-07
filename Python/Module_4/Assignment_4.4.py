"""
4. While loops (while)
    4.4. Write a game where the computer draws a random integer between 1 and
         10.

         The user tries to guess the number until they guess the right number.

         After each guess the program prints out a text:
            Too high, Too low or Correct.
         Notice that the computer must not change the number between guesses.

"""

from random import randint

number = randint(1, 10)

guess = 0

print('I have a number between 1 and 10.')

while number != guess:
    guess = int(input('Please guess the number:\n'))
    if number < guess:
        print('Too high')
    elif number > guess:
        print('Too low')
    else:
        print('Correct')
