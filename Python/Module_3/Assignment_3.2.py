"""
3. Conditional structures (if)

    3.2. Write a program that asks the user to enter the cabin class of a
         cruise ship and then prints out a written description according to the
         list below. You must use an if/elif/else structure in your solution.

             - LUX: upper-deck cabin with a balcony.
             - A: above the car deck, equipped with a window.
             - B: windowless cabin above the car deck.
             - C: windowless cabin below the car deck.

         If the user enters an invalid cabin class, the program outputs an
         error message Invalid cabin class.
"""

cabin_class = input(
    "Could you please input the cabin class of the cruise ship?\n"
    "Your cabin class: ").upper()


if cabin_class == 'LUX':
    print('Wow, A great cabin. This is an upper-deck cabin with a balcony.')

elif cabin_class == 'A':
    print('This is a cabin above the car deck, equipped with a window.')

elif cabin_class == 'B':
    print('This is a cabin above the car deck, without a window.')

elif cabin_class == 'C':
    print('This is a cabin below the car deck, without a window.')

else:
    print('Invalid cabin class')
