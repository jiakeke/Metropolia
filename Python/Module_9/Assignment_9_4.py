"""
9. Fundamentals of object-oriented programming

    9.4. Now we will program a car race. The travelled distance of a new car is
         initialized as zero. At the beginning of the main program, create a
         list that consists of 10 car objects created using a loop. The maximum
         speed of each new car is a random value between 100 km/h and 200 km/h.
         The registration numbers are created as follows: "ABC-1", "ABC-2" and
         so on. Now the race begins. One per every hour of the race, the
         following operations are performed:

         - The speed of each car is changed so that the change in speed is
           a random value between -10 km/h and +15 km/h. This is done using the
           accerelate method.

         - Each car is made to drive for one hour. This is done with the drive
           method.

         The race continues until one of the cars has advanced at least 10,000
         kilometers. Finally, the properties of each car are printed out
         formatted into a clear table.
"""

import os, sys, time
sys.path.append("..")
print(sys.path)
from random import randint
from tabulate import tabulate
from Module_9.Assignment_9_3 import CarBeta


class CarGamma(CarBeta):
    pass


def clear_screen():
    os_name = sys.platform.lower()
    if os_name.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    cars = []
    for num in range(1, 11):
        car = CarGamma(f'ABC-{num}', randint(100, 200))
        cars.append(car)

    hours = 0
    is_finished = False
    while is_finished == False:
        hours += 1
        time.sleep(0.1)
        clear_screen()
        print(f'The game lasted {hours} hours.')
        for car in cars:
            if not is_finished:
                car.accelerate(randint(-10, 15))
                car.drive(1)
            print('-'*(car.distance//100), f'[{car.plate}]')
            if car.distance >= 10000:
                is_finished = True
                #break

    print(f'The final ranking.')

    properties = ['plate', 'max_speed', 'speed', 'distance']
    header = ['Rank'] + [item.replace('_', ' ').title() for item in properties]
    content = []
    cars.sort(key=lambda car: car.distance, reverse=True)
    for num, car in enumerate(cars, 1):
        row = [num] + [getattr(car, prop, '') for prop in properties]
        content.append(row)
    ranking_table = tabulate(content, header, tablefmt="grid")
    print(ranking_table)

