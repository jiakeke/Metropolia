"""
6. Functions

    6.5. Write a function that gets a list of integers as a parameter. The
         function returns a second list that is otherwise the same as the
         original list except that all uneven numbers have been removed.
         For testing, write a main program where you create a list, call the
         function, and then print out both the original as well as the cut-down
         list.

"""
from random import randint

def remove_odd(numbers):
    results = []
    for number in numbers:
        if number % 2 == 0:
            results.append(number)
    return results

start = randint(0, 20)
end = randint(start+10, start+30)

numbers = list(range(start, end))
evens = remove_odd(numbers)

print(f'Original list: {numbers}')
print(f'Cut-down list: {evens}')


