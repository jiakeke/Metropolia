"""
2. Variables and interactive programs

    2.3. Write a program that asks the user for the length and width of a
         rectangle. The program then prints out the perimeter and area of the
         rectangle. The perimeter of a rectangle is the sum of the lengths of
         each four sides.

"""

print(
    'Please input the length and width of a rectangle. '
    'Then I can calculate the perimeter and area of the rectangle.'
)
length = float(input('Length: '))
width = float(input('Width: '))

perimeter = length*2 + width*2
area = length * width

print(f'The perimeter of the rectangle is: {perimeter:.2f}')
print(f'The area of the rectangle is: {area:.2f}')
