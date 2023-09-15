"""
6. Functions

    6.3. Write a function that gets the quantity of gasoline in American
         gallons and returns the number converted to litres. Write a main
         program that asks for a volume in gallons from the user and converts
         the value to liters. The conversion must be done by using the
         function. Conversions continue until the user inputs a negative value.

"""

gallon_to_liter = 3.78541178

def convert_gallon_to_liter(number):
    return round(number*gallon_to_liter, 2)

while True:
    number = input(
        "Please input the quantity of gasoline in American gallons, "
        "leave blank to quit: ")
    if not number:
        break

    try:
        number = int(number)
    except ValueError:
        try:
            number = float(number)
        except ValueError:
            print("Please input an valid number or leave blank to quit")
            continue

    number_liter = convert_gallon_to_liter(number)
    print(f"{number} gallons = {number_liter} liters")


