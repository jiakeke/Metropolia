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
