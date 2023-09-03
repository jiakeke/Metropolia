"""
2. Variables and interactive programs

    2.4. Write a program that asks the user for three integer numbers.
         The program prints out the sum, product, and average of the numbers.

"""

print(
    'Please input three integer numbers. '
    'Then I would calculate the sum, product, and average for you.'
)

num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
num3 = int(input('Number 3: '))


the_sum = num1 + num2 + num3
the_product = num1 * num2 * num3
the_average = round(the_sum / 3, 2)

print(f'The sum: {the_sum}, product: {the_product}, average: {the_average}')
