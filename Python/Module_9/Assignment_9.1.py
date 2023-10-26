"""
9. Fundamentals of object-oriented programming

    9.1. Write a Car class that has the following properties: registration
         number, maximum speed, current speed and travelled distance.
         Add a class initializer that sets the first two of the properties
         based on parameter values. The current speed and travelled distance of
         a new car must be automatically set to zero. Write a main program
         where you create a new car (registration number ABC-123, maximum speed
         142 km/h). Finally, print out all the properties of the new car.
"""

class Car:
    current_speed = 0
    distance = 0

    def __init__(self, plate_number, max_speed):
        self.plate_number = plate_number
        self.max_speed = max_speed

    def __str__(self):
        return (
            f'Car:\n'
            f'    Plate number: {self.plate_number}\n'
            f'    Maximum speed: {self.max_speed} km/h\n'
            f'    Current speed: {self.current_speed} km/h\n'
            f'    Rravelled distance: {self.distance} km\n'
            )

car = Car('ABC-123', 142)
print(car)
