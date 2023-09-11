print('Please input two numbers, then I can give you the the sum of them.')

answer = 'Yes'
lst = []
while answer.lower() != 'no':
    num1 = int(input('Number 1: '))
    num2 = int(input('Number 2: '))
    lst.append((num1, num2))
    answer = input('Would you like to continue? (Yes or No)')

for num1, num2 in lst:
    print(f'The sum of {num1} and {num2} is {num1+num2}.')

