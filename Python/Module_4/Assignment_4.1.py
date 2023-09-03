"""
4. While loops (while)

    4.1. Write a program that uses a while loop to print out all numbers
         divisible by three in the range of 1-1000.

"""

number = 1
end = 1000
while number <= end:
    if number % 3 == 0:
        msg = '{:>%s} ' % len(str(end))
        print(msg.format(number), end='')
    if number % 30 == 0:
        print()
    number += 1

print()
