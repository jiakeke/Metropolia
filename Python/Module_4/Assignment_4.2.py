"""
4. While loops (while)

    4.2. Write a program that converts inches to centimeters until the user
         inputs a negative value. Then the program ends.

    1 inch = 2.54 cm

"""

length_inch = 0

while length_inch >= 0:
    try:
        length_inch = float(input(
            'Please input a length in inches and I can convert it to centimeters '
            'for you. Input a negative number to exit.\n'
        ))
        if length_inch >= 0:
            length_cm = length_inch * 2.54
            print(f'{length_inch} inch = {length_cm} cm')
        else:
            print('Program Exit, Bye...')
    except ValueError:
        print('Please enter a valid non-negative real number.')

