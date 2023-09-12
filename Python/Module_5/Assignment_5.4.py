"""
5. List structures and iterative loops (for)

    5.4. Write a program that asks the user to enter the names of five cities
         one by one (use a for loop for reading the names) and stores them into
         a list structure. Finally, the program prints out the names of the
         cities one by one, one city per line, in the same order they were read
         as input. Use a for loop for asking the names and a for/in loop to
         iterate through the list.

"""

cities = []
for num in range(1, 6):
    city = input(f'Please input five cities one by one.\n{num}: ')
    cities.append(city)

print('Here are the cities: ')
for num, city in enumerate(cities, start=1):
    print(f'{num}. {city}')
