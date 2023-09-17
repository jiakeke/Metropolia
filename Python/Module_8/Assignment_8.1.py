"""
8. Using relational databases

    8.1. Write a program that asks the user to enter the ICAO code of an
         airport. The program fetches and prints out the corresponding airport
         name and location(town) from the airport database used on this course.
         The ICAO codes are stored in the ident column of the airport table.

"""

import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='test',
         user='gary',
         password='mypass',
         autocommit=True
         )


def select_all_as_dict(tbl_name, **kws):
    keywords = ' and '.join(["%s='%s'" % (k, v) for k, v in kws.items()])
    sql = "select * from %s where %s;" % (tbl_name, keywords)
    cursor = connection.cursor()
    cursor.execute(sql)
    names = cursor.column_names
    result = cursor.fetchall()
    tmp = []
    if cursor.rowcount >0 :
        for row in result:
            obj = dict(zip(names, row))
            tmp.append(obj)
    return tmp

def get_airports(**kws):
    return select_all_as_dict('airport', **kws)


while True:
    print('Please input ICAO code, leave a blank to quit.')
    icao_code = input('ICAO code: ')
    if not icao_code:
        break
    airports = get_airports(ident=icao_code)

    if airports:
        for airport in airports:
            print(f"Name: {airport['name']}")
            print(f"Location: {airport['municipality']}\n")

    else:
        print('Airport not found!\n')
