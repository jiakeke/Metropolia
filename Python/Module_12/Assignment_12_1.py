"""
12. Using external interfaces

    12.1. Write a program that fetches and prints out a random Chuck Norris
          joke for the user.
          Use the API presented here: https://api.chucknorris.io/.
          The user should only be shown the joke text.
"""

import requests

api_url = 'https://api.chucknorris.io/jokes/random'
req = requests.get(api_url)
if req.status_code == 200:
    print(req.json()['value'])
