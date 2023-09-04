"""
4. While loops (while)

    4.3. Write a program that asks the user to enter numbers until they enter
         an empty string to quit. Finally, the program prints out the smallest
         and largest number from the numbers it received.

"""

smallest = False
largest = 0

running = True
while running:
    number = input(
        'Please input numbers one by one, either integer or decimal. '
        'Leave an empty string to quite:\n'
    )
    if number.strip() == '':
        running = False

    else:
        try:
            number = int(number)
        except ValueError:
            try:
                number = float(number)
            except ValueError:
                print('Please input a valid number, either integer or decimal.')
                continue

        if smallest is False:
            smallest = number
        elif number < smallest:
            smallest = number
        if number > largest:
            largest = number

print(f'The smallest number is {smallest}, the largest one is {largest}.')

