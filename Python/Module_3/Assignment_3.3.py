"""
3. Conditional structures(if)

    3.3. Write a program that asks for the biological gender and hemoglobin
         value (g/l). The program the notifies the user if the hemoglobin value
         is low, normal or high.

        - A normal hemoglobin value for adult females is between 117-155 g/l.
        - A normal hemoglobin value for adult males is between 134-167 g/l.
"""

gender = ''
gender_mapping = {'m': 'male', 'male': 'male', 'f': 'female', 'female': 'female'}
while gender not in gender_mapping:
    gender = input(
        'Please input your biological gender.\n'
        'Female(F) or Male(M): ').lower()

gender = gender_mapping.get(gender, 'female')

value = int(input('Please input your hemoglobin value (g/l).\nHemoglobin Value: '))

msg_high = f'As a {gender}, your hemoglobin value is: High'
msg_low = f'As a {gender}, your hemoglobin value is: Low'
msg_normal = f'As a {gender}, your hemoglobin value is: Normal'

if gender == 'female':
    if value > 155:
        print(msg_high)
    elif value < 117:
        print(msg_low)
    else:
        print(msg_normal)
else:
    if value > 167:
        print(msg_high)
    elif value < 134:
        print(msg_low)
    else:
        print(msg_normal)
