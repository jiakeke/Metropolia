"""
6. Functions

    6.6. Write a function that receives two parameters: the diameter of a round
         pizza in centimeters and the price of the pizza in euros. The function
         calculates and returns the unit price of the pizza per square meter.
         The main program asks the user to enter the diameter and price of two
         pizzas and tells the user which pizza provides better value for money
         (which of them has a lower unit price). You must use the function you
         wrote for calculating the unit prices.

"""
from math import pi

def get_unit_price(diameter, price):
    area = pi * (0.5*float(diameter)/100)**2
    unit_price = float(price)/area
    return unit_price


while True:

    print('======================')
    print('Pizza Price Calculator')
    print('======================')

    diameter_1 = input("Please input the diameter of the first pizza: ")
    price_1 = input("Please input the price of the first pizza in euros: ")

    diameter_2 = input("Please input the diameter of the second pizza: ")
    price_2 = input("Please input the price of the second pizza in euros: ")

    try:
        unit_price_1 = get_unit_price(diameter_1, price_1)
        unit_price_2 = get_unit_price(diameter_2, price_2)
    except ValueError:
        print('Please input a valid number for the price or diameter')
        continue

    if unit_price_1 < unit_price_2:
        lower = 'first'
    else:
        lower = 'second'

    print(f'The {lower} pizza provides better value for money')

    option = input('Would you like to continue? (Y/N)')
    if option.lower() == 'n':
        break
