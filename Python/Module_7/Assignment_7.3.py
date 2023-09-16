"""
7. Tuple, set, and dictionary

    7.3. Write a program for fetching and storing airport data. The program
         asks the user if they want to enter a new airport, fetch the
         information of an existing airport or quit. If the user chooses to
         enter a new airport, the program asks the user to enter the ICAO code
         and name of the airport. If the user chooses to fetch airport
         information instead, the program asks for the ICAO code of the airport
         and prints out the corresponding name. If the user chooses to quit,
         the program execution ends. The user can choose a new option as many
         times they want until they choose to quit. (The ICAO code is an
         identifier that is unique to each airport. For example, the ICAO code
         of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes
         of different airports online.)

"""

def print_header(title, desc):
    print(f"{'='*15} {title.upper()} {'='*15}")
    print(desc.capitalize())

airports = {'EFHK': 'Helsinki-Vantaa'}

options = (
    'Enter a new airport.',
    'Fetch the information of an existing airport.',
    'Quit.',
    )


while True:
    print_header('menu', 'Options:')

    for num, option in enumerate(options, start=1):
        print(f'{num}. {option}')

    option = input('Please choose your option above: ')
    if option == '1':
        print_header(
            'input new airport',
            'please enter the ICAO code and name of the airport'
        )
        icao_code = input('ICAO code: ')

        if icao_code not in airports:
            name = input('Name: ')
            airports[icao_code] = name
        else:
            print('The airport is exit.')

    elif option == '2':
        print_header(
            'search airport',
            'please enter the ICAO code to search the airport'
        )
        icao_code = input('ICAO code: ')
        if icao_code in airports:
            print(f'Name: {airports[icao_code]}')
        else:
            print('The airport is not exit.')

    elif option == '3':
        break

    else:
        print('Please input an valid option')
