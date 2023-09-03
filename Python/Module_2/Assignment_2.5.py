"""
2. Variables and interactive programs

    2.5. Write a program that asks the user to enter a mass in medieval units:
         talents (leiviskä), pounds (naula), and lots (luoti). The program
         converts the input to full kilograms and grams and outputs the result
         to the user:

             - One talent is 20 pounds.
             - One pound is 32 lots.
             - One lot is 13,3 grams.

"""

talents = float(input('Enter talents: \n'))
print()
pounds = float(input('Enter pounds: \n'))
print()
lots = float(input('Enter lots: \n'))

weight = ((talents*20 + pounds)*32 + lots)*13.3

weight_kg = int(weight // 1000)
weight_g = round(weight % 1000, 2)

print()
print('The weight in modern units:')
print(f'{weight_kg} kilograms and {weight_g} grams.')
