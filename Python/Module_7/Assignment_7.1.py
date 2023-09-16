"""
7. Tuple, set, and dictionary

    7.1. Write a program that asks the user for a number of a month and then
         prints out the corresponding season (spring, summer, autumn, winter).
         Save the seasons as strings into a tuple in your program.
         We can define each season to last three months, December being the
         first month of winter.

"""

seasons = ('spring', 'summer', 'autumn', 'winter')

while True:
    month = input(
        'Please input the number of a month. '
        '(e.g. 1-12, input 0 to quit.)\n')

    if month == '0':
        break

    if month.isnumeric():
        month = int(month)
        season = seasons[(month-3)//3]
        print(f'It is {season.capitalize()}')
    else:
        print('Please in put a valid number of a month. (e.g. 1-12)')

