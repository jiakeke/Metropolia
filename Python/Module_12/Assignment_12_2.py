"""
12. Using external interfaces

    12.2. Familiarize yourself with the OpenWeather weather API at:
                https://openweathermap.org/api.
          Your task is to write a program that asks the user for the name of a
          municipality and then prints out the corresponding weather condition
          description text and temperature in Celsius degrees. Take a good look
          at the API documentation. You must register for the service to
          receive the API key required for making API requests. Furthermore,
          find out how you can convert Kelvin degrees into Celsius.
"""

import requests

api_key = 'PLEASE_PROVIDE_A_CORRECT_API_KEY'

if __name__ == '__main__':

    while 1:
        print(
            'Please input your city name to get the weachter information'
            'Leave a blank to quit.'
        )

        city = input('City: ')

        if not city:
            break

        weather_api_url = (
            'https://api.openweathermap.org/data/2.5/weather?units=metric'
            f'&q={city}'
            f'&appid={api_key}'

        )
        req_weather = requests.get(weather_api_url)
        if req_weather.status_code == 200:
            data_weather = req_weather.json()
            weather = data_weather['weather'][0]
            main = weather['main']
            description = weather['description']
            temp = data_weather['main']['temp']
            print(f'The weather of {city}:')
            print(f'    Weather: {main}, {description}')
            print(f'    Temperature: {temp}')
        else:
            print(f'{req_weather.reason}: ')
            print(req_weather.json()['message'])
