"""
3. Conditional structures (if)

    3.1. Write a program that asks a fisher the length of a zander in
         centimeters. If the zander does not fulfill the size limit, the
         program instructs to release the fish back into the lake and notifies
         the user of how many centimeters below the size limit the caught fish
         was. A zander must be 42 centimeters or longer to meet the size limit.
"""

size_limit = 42

length = int(input('How many centimeters is the zander you caught?\n'))

if length >= size_limit:
    print('Congratulations! You caught a big fish')
else:
    print(
        "Unfortunately, the fish you caught didn't fullfill the minimum size "
        f"limit, it was {size_limit-length} cm short and you have to release "
        "it back into the lake."
    )
