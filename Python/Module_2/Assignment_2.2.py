"""
2. Variables and interactive programs
    2.2. Write a program that asks the user for the radius of a circle and the
         prints out the area of the circle.

"""

import math


radius = float(input('Please input the radius of a circle: '))

area = math.pi*radius**2

print(f'The area of your circle is: {area:.3f}')
