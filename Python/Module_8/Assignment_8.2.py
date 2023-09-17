"""
8. Using relational databases

    8.2. Write a program that asks the user to enter the area code (for example
         FI) and prints out the airports located in that country ordered by
         airport type. For example, Finland has 65 small airports, 15
         helicopter airports and so on.

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


def select_all_as_dict(tbl_name, sort_by='', **kws):
    conditions = ' and '.join(["%s='%s'" % (k, v) for k, v in kws.items()])

    order_by = ''
    if sort_by:
        order_by = f' order by {sort_by}'

    sql = f"select * from {tbl_name} where {conditions}{order_by};"
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


def get_airports_by_country_code(iso_country):
    return select_all_as_dict('airport', sort_by='type', iso_country=iso_country)


def print_airports(airports):
    keys = [
            ('ident', 10),
            ('type', 15),
            ('iso_country', 12),
            ('name', 50),
    ]

    headers = []
    for key, width in keys:
        headers.append(f'{key.upper():{width}s}')
    print(' '.join(headers))
    print('-'*80)

    for airport in airports:
        rows = []
        for key, width in keys:
            value = airport[key]
            rows.append(f'{value:{width}s}')
        print(' '.join(rows))

    print('-'*80)
    print(f'Totally {len(airports)} airports.\n')

while True:
    print('Please input country code, leave a blank to quit.')
    country_code = input('Country code(e.g. FI): ')
    if not country_code:
        break
    airports = get_airports_by_country_code(country_code)

    if airports:
            print_airports(airports)
            #print(f"Name: {airport['name']}")
            #print(f"Location: {airport['municipality']}\n")

    else:
        print('Airport not found!\n')

