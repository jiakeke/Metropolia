"""
11. Inheritance

    11.2. Extend the previosly written Car class by adding two subclasses:
          ElectricCar and GasolineCar. Electric cars have the capacity of the
          battery in kilowatt-hours as their property. Gasoline cars have the
          volume of the tank in liters as their property. Write initializers
          for the subclasses. For example, the initializer of electric cars
          receives the registration number, maximum speed and battery capacity
          as its parameter. It calls the initializer of the base class to set
          the first two properties and then sets its capacity. Write a main
          program where you create one electric car(ABC-15, 180 km/h, 52.5 kWh)
          and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for
          both cars, make them drive for three hours and print out the values
          of their kilometer counters.
"""

import os, sys, time
sys.path.append("..")
import time
from random import randint
from tabulate import tabulate
from Module_9.Assignment_9_4 import CarGamma
from Module_9.Assignment_9_4 import clear_screen
from Module_10.Assignment_10_4 import Race


class ElectricCar(CarGamma):

    def __init__(self, plate, max_speed, capacity):
        super().__init__(plate, max_speed)
        self.capacity = capacity


class GasolineCar(CarGamma):

    def __init__(self, plate, max_speed, volume):
        super().__init__(plate, max_speed)
        self.volume = volume


if __name__ == '__main__':
    electric_car = ElectricCar('ABC-15', 180, 52.5)
    gasoline_car = GasolineCar('ACD-123', 165, 32.3)
    cars = [electric_car, gasoline_car]

    race = Race('Electric VS. Gasoline', 10000, cars)
    race.race_start()
