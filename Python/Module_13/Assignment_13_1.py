"""
13. Setting up a backend service with an interface

    13.1. Implement a Flask backend service that tells whether a number
          received as a parameter is a prime number or not. Use the prior prime
          number exercise as a starting point. For example, a GET request for
          number 31 is given as: http://127.0.0.1:5000/prime_number/31.
          The response must be in the format of {"Number":31, "isPrime":true}.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/prime_number/<int:number>")
def prime_number(number):
    if number == 1:
        isPrime = False

    else:
        for num in range(2, int(number**0.5)+1):
            if number % num == 0:
                isPrime = False
                break
        else:
            isPrime = True
    context = {'Number': number, 'isPrime': isPrime}
    return context
