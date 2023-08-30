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
