"""
10. Association
    10.1. Write an Elevator class that receives the numbers of the bottom and
          top floors as initializer parameters. The elevator has methods
          go_to_floor, floor_up and floor_down. A new elevator is always at the
          bottom floor. If you make elevator h for example the method call
          h.go_to_floor(5), the method calls either the floor_up or floor_down
          methods as many times as it needs to get to the fifth floor.
          The methods run the elevator one floor up or down and tell what floor
          the elevator is after each move. Test the class by creating an
          elevator in the main program, tell it to move to a floor of your
          choice and then back to the bottom floor.

"""

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    @property
    def Current(self):
        postfix = {1: 'st', 2: 'nd', 3: 'rd'}.get(abs(self.current) % 10, 'th')
        return f'It\'s the {self.current}{postfix} floor.'

    def go_to_floor(self, target):
        if target > self.top or target < self.bottom:
            print('The floor you entered does not exist')
            return

        if target > self.current:
            quantity = target - self.current
            move = self.floor_up
        elif target < self.current:
            quantity = self.current - target
            move = self.floor_down
        else:
            quantity = 0
            move = None

        if quantity:
            for _ in range(quantity):
                move()
        else:
            print(self.Current)


    def go_to_bottom(self):
        self.go_to_floor(self.bottom)


    def floor_up(self):
        self.current = min(self.current + 1, self.top)
        print(self.Current)

    def floor_down(self):
        self.current = max(self.current - 1, self.bottom)
        print(self.Current)


if __name__ == '__main__':
    elevator = Elevator(-2, 10)
    elevator.go_to_floor(10)
    elevator.go_to_floor(12)
    elevator.go_to_floor(5)
    elevator.go_to_bottom()

