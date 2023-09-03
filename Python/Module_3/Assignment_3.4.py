"""
3. Conditional structures(if)

    3.4. Write a program that asks the user to enter a year and notifies the
         user whether the input year is a leap year. A year is a leap year if
         it is divisible by four. However, years divisible by 100 are leap
         years only if they are also divisible by 400.
"""

year = int(input('Please input a year: '))
year_type = 'common'

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            year_type = 'leap'
    else:
        year_type = 'leap'

print(f'{year} is a {year_type} year.')
