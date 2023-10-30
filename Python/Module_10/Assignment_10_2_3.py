"""
10. Association
    10.2. Extend the previous program by creating a Building class.
          The initializer parameters for the class are the numbers of the
          bottom and top floors and the number of elevators in the building.
          When a building is created, the building creates the required number
          of elevators. The list of elevators is stored as a property of the
          building. Write a method called run_elevator that accepts the number
          of the elevator and the destination floor as its parameters.
          In the main program, write the statements for creating a new building
          and running the elevators of the building.

    10.3. Extend the program again by adding a method fire_alarm that does not
          receive any parameters and moves all elevators to the bottom floor.
          Continue the main program by causing a fire alarm in your building.
"""

from Assignment_10_1 import Elevator


class Building:
    def __init__(self, bottom, top, number_of_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for _ in range(number_of_elevators):
            ele = Elevator(bottom, top)
            self.elevators.append(ele)
            ele.building = self

    def run_elevator(self, number, target):
        if number >= len(self.elevators) or number < 0:
            print(
                 'The elevator number you entered does not exist. There are '
                f'{len(self.elevators)} elevators in this building to choose '
                 'from. Please enter the elevator number from 0 to '
                f'{len(self.elevators)-1} to select the elevator you want to '
                 'take.'
            )
            return
        return self.elevators[number].go_to_floor(target)

    def fire_alarm(self):
        print('Fire Alarm! The elevators would be closed.')
        for elevator in self.elevators:
            elevator.go_to_bottom()


if __name__ == '__main__':
    building = Building(-2, 10, 3)
    building.run_elevator(2, 9)
    building.run_elevator(7,  45)
    building.run_elevator(1,  45)
    building.fire_alarm()
