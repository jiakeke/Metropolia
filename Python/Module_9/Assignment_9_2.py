"""
9. Fundamentals of object-oriented programming

    9.2. Extend the program by adding an accerelate method into the new class.
         The method should receive the change of speed (km/h) as a parameter.
         If the change is negative, the car reduces speed. The method must
         change the value of the speed property of the object. The speed of the
         car must stay below the set maximum and cannot be less than zero.
         Extend the main program so that the speed of the car is first
         increased by +30 km/h, then +70 km/h and finally +50 km/h.
         Then print out the current speed of the car. Finally, use the
         emergency brake by forcing a -200 km/h change on the speed and then
         print out the final speed. The travelled distance does not have to be
         updated yet.
"""
import sys
sys.path.append("..")
from Module_9.Assignment_9_1 import Car


class CarAlpha(Car):

    def accelerate(self, change):
        speed = self.speed + change
        self.speed = min(max(0, speed), self.max_speed)


if __name__ == "__main__":
    car = CarAlpha('ABC-123', 142)
    print(car)

    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print(car)

    car.accelerate(-200)
    print(car)
