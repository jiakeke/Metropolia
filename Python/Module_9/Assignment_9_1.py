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
    speed = 0
    distance = 0

    def __init__(self, plate, max_speed):
        self.plate = plate
        self.max_speed = max_speed

    def __str__(self):
        return (
            f'Car:\n'
            f'    Plate number: {self.plate}\n'
            f'    Maximum speed: {self.max_speed} km/h\n'
            f'    Speed: {self.speed} km/h\n'
            f'    Travelled distance: {self.distance} km\n'
            )

if __name__ == "__main__":
    car = Car('ABC-123', 142)
    print(car)
