"""
2. Variables and interactive programs

    2.6. Write a program that draws two random combinations of numbers for a
         combination lock:

             - a 3-digit code where each number is between 0 and 9.
             - a 4-digit code where each number is between 1 and 6.

"""

from random import randint

three_digits = ''.join([str(randint(0, 9)) for item in range(3)])
four_digits = ''.join([str(randint(1, 6)) for item in range(4)])

print(f'The 3-digit code: {three_digits}')
print(f'The 4-digit code: {four_digits}')
