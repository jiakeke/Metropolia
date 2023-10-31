"""
9. Fundamentals of object-oriented programming

    9.3. Again, extend the program by adding a new drive method that receives
         the number of hours as a parameter. The method increases the travelled
         distance by how much the car has travelled in constant speed in the
         given time. Example: The travelled distance of car object is 2000 km.
         The current speed is 60 km/h. Method call car.drive(1.5) increases the
         travelled distance to 2090 km.
"""

import sys
sys.path.append("..")
from Module_9.Assignment_9_2 import CarAlpha


class CarBeta(CarAlpha):

    def drive(self, hours):
        self.distance += self.speed * hours


if __name__ == "__main__":
    car = CarBeta('ABC-123', 142)
    print(car)

    car.accelerate(60)
    car.drive(1.5)
    print(car)
