from random import randint

three_digits = ''.join([str(randint(0, 9)) for item in range(3)])
four_digits = ''.join([str(randint(1, 6)) for item in range(4)])

print(f'The 3-digit code: {three_digits}')
print(f'The 4-digit code: {four_digits}')
