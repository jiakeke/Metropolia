"""
5. List structures and iterative loops (for)

    5.2. Write a program that asks the user to enter numbers until they input
         an empty string to quit. At the end, the program prints out the five
         greatest numbers sorted in descending order.

         Hint: You can reverse the order of sorted list items by using the sort
         method with the reverse=True argument.

"""

results =  []

while True:
    number = input('Please input numbers or input an empty character to exit.\n')
    if number == '':
        break

    results.append(int(number))

results.sort(reverse=True)

print('The five greatest numbers are:')
print('\n'.join(map(str, results[:5])))
