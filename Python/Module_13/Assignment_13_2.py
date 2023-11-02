"""
13. Setting up a backend service with an interface

    13.2. Implement a backend service that gets the ICAO code of an airport and
          then returns the name and location of the airport in JSON format. The
          information is fetched from the airport database used on this course.
          For example, the GET request for EFHK would be:
              http://127.0.0.1:5000/airport/EFHK

          The response must be in the format of:
              {
                  "ICAO": "EFHK",
                  "Name": "Helsinki-Vantaa Airport",
                  "Location":"Helsinki"
              }.
"""

from flask import Flask
import mysql.connector


connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='test',
         user='gary',
         password='mypass',
         autocommit=True
         )


app = Flask(__name__)

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

@app.route("/airport/<icao>")
def airport(icao):
    airports = get_airports(ident=icao)
    if len(airports) > 0:
        context = {
            'ICAO': icao,
            'Name': airports[0]['name'],
            'Location':airports[0]['municipality']
        }
        return context
    return {'ICAO': icao, 'Status': 'Not Found'}
