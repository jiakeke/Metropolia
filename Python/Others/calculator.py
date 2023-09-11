
def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    print('Zero cannot be used as a divisor')

def calculate(a, b, method, symbol):
    res = method(num1, num2)
    if res is None:
        return
    print(f'{num1} {symbol} {num2} = {res}')

print(
    'Please input two numbers, '
    'then I can calculate the sum, difference, product and quotient for you.'
)

answer = 'Yes'

calculator = [(sum, '+'), (subtract, '-'), (multiply, 'x'), (divide, '÷')]

while answer.lower() != 'no':
    num1 = int(input('Number 1: '))
    num2 = int(input('Number 2: '))
    for n, (method, symbol) in enumerate(calculator):
        print(f'{n} for {symbol}')

    print(f'4 for all')
    cal_num = int(input('Which calculation would you like? '))

    if cal_num < 4:
        calculate(num1, num2, method, symbol)

    else:
        for method, symbol in calculator:
            calculate(num1, num2, method, symbol)
    answer = input('Would you like to continue? (Yes or No)')

