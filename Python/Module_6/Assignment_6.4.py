"""
6. Functions

    6.4. Write a function that gets a list of integers as a parameter. The
         function returns the sum of all the numbers in the list. For testing,
         write a main program where you create a list, call the function, and
         print out the value it returned.

"""


def get_sum(numbers):
    try:
        return sum(numbers)
    except:
        pass


numbers = range(11)
amount = get_sum(numbers)

print(f'The sum of {list(numbers)} is: {amount}')
