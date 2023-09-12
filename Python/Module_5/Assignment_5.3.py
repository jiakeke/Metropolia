"""
5. List structures and iterative loops (for)

    5.3. Write a program that asks the user for an integer and tells if the
         number is a prime number. Prime numbers are number that are only
         divisible by one or the number itself.

             - For example, 13 is a prime number as it can only be divided by 1
               or 13 so that the result is an integer.

             - On the other hand, 21 is not a prime number as it is divisible
               by 3 and 7.

"""

while True:

    number = input(
        'Please input an integer and I can tell you whether it is a prime '
        'number. Input an empty character to exit.\n'
    )
    if number == '':
        break

    number = int(number)
    if number == 1:
        print(f'The number {number} is not a prime number.')
        continue

    for num in range(2, int(number**0.5)+1):
        if number % num == 0:
            print(f'The number {number} is not a prime number.')
            break
    else:
        print(f'The number {number} is a prime number.')
