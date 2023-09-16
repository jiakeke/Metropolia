"""
7. Tuple, set, and dictionary

    7.2. Write a program that asks the user to enter names until he/she enters
         an empty string. After each name is read the program either prints out
         New name or Existing name depending on whether the name was entered
         for the first time. Finally, the program lists out the input names one
         by one, one below another in any order. Use the set data structure to
         store the names.

"""

names = set()

while True:
    name = input('Please input a name. Leave a blank to quit.\n')

    if not name:
        break

    if name in names:
        print('Existing name')
    else:
        print('New name')
        names.add(name)

print('Here are all of the names.')
for name in names:
    print(name)
