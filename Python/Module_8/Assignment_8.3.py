"""
8. Using relational databases

    8.3. Write a program that asks the user to enter the ICAO codes of two
         airports. The program prints out the distance between the two airports
         in kilometers. The calculation is based on the airport coordinates
         fetched from the database. Calculate the distance using the geopy
         library: https://geopy.readthedocs.io/en/stable/. Install the library
         by selecting View / Tool Windows / Python Packages in your PyCharm
         IDE, write geopy into the search field and finish the installation.

"""

import mysql.connector
from geopy import distance


connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='test',
         user='gary',
         password='mypass',
         autocommit=True
         )


def select_one_as_dict(tbl_name, sort_by='', **kws):
    conditions = ' and '.join(["%s='%s'" % (k, v) for k, v in kws.items()])

    order_by = ''
    if sort_by:
        order_by = f' order by {sort_by}'

    sql = f"select * from {tbl_name} where {conditions}{order_by};"
    cursor = connection.cursor()
    cursor.execute(sql)
    names = cursor.column_names
    result = cursor.fetchone()
    obj = None
    if result :
        obj = dict(zip(names, result))
    return obj


def get_airport_coordinate(**kws):
    airport = select_one_as_dict('airport', **kws)
    if airport:
        coordinate = (airport['latitude_deg'], airport['longitude_deg'])
        return coordinate


while True:
    print('Please input two ICAO code, leave a blank to quit.')

    icao_code_1 = input('ICAO code 1: ')
    icao_code_2 = input('ICAO code 2: ')

    if not icao_code_1 or not icao_code_2:
        break

    coordinate1 = get_airport_coordinate(ident=icao_code_1)
    coordinate2 = get_airport_coordinate(ident=icao_code_2)
    if coordinate1 and coordinate2:
        distance_km = distance.distance(coordinate1, coordinate2).km
        print(f'The distance of the two airports is {distance_km} km.\n')
    else:
        print('Please input two valid airports.\n')

