"""

    10.4. This exercise continues the previous car race exercise from the last
          exercise set. Write a Race class that has the following properties:
          name, distance in kilometers and a list of cars participating in the
          race. The class has an initializer that receives the name,
          kilometers, and car list as parameters and sets their values to the
          corresponding properties in the class. The class has the following
          methods:

            * hour_passes, which performs the operations done once per hour in
              the original exercise: generates a random change of speed for
              each car and calls their drive method.

            * print_status, which prints out the current information of each
              car as a clear, formatted table.

            * race_finished, which returns True if any of the cars has reached
              the finish line, meaning that they have driven the entire
              distance of the race.

          Write a main program that creates an 8000-kilometer race called Grand
          Demolition Derby. The new race is given a list of ten cars similarly
          to the earlier exercise. The main program simulates the progressing
          of the race by calling the hour_passes in a loop, after which it uses
          the race_finished method to check if the race has finished. The
          current status is printed out using the print_status method every ten
          hours and then once more at the end of the race.
"""
import sys
sys.path.append("..")
import time
from random import randint
from tabulate import tabulate
from Module_9.Assignment_9_4 import CarGamma
from Module_9.Assignment_9_4 import clear_screen


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def race_start(self):
        hours = 0
        while race.race_finished() == False:
            hours += 1
            time.sleep(0.1)
            clear_screen()
            print(f'The race lasted {hours} hours.')
            self.hour_passes()
            if hours % 10 == 0:
                self.print_status()
                time.sleep(1)

        self.print_status()

    def hour_passes(self):
        for car in self.cars:
            if not self.race_finished():
                car.accelerate(randint(-10, 15))
                car.drive(1)
            print('-'*(car.distance//100), f'[{car.plate}]')

    def print_status(self):
        print(f'The final ranking.')

        properties = ['plate', 'max_speed', 'speed', 'distance']
        header = ['Rank'] + [item.replace('_', ' ').title() for item in properties]
        content = []
        self.cars.sort(key=lambda car: car.distance, reverse=True)
        for num, car in enumerate(self.cars, 1):
            row = [num] + [getattr(car, prop, '') for prop in properties]
            content.append(row)
        ranking_table = tabulate(content, header, tablefmt="grid")
        print(ranking_table)

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False

if __name__ == '__main__':
    cars = []
    for num in range(1, 11):
        car = CarGamma(f'ABC-{num}', randint(100, 200))
        cars.append(car)

    race = Race('Grand Demolition Derby', 8000, cars)
    race.race_start()

