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

        geo_api_url = (
            f'http://api.openweathermap.org/geo/1.0/direct?q={city}'
            f'&limit=5&appid={api_key}'
        )

        req_city = requests.get(geo_api_url)
        error_text = req_city.json()
        if req_city.status_code == 401 and \
           error_text['message'].startswith('Invalid API'):
            print(f"{error_text['cod']}: {error_text['message']}\n")
            print("Warning!\n")
            print(
                "It's not good idea to submit some SECRET information into\n"
                "github. Since it's published to everyone. So if you want to\n"
                "run the program correctly, please change the api_key at the\n"
                "top of the program file to the correct value.\n"
            )
        if req_city.status_code == 200:
            data = req_city.json()
            name = data[0]['name']
            lat = data[0]['lat']
            lon = data[0]['lon']
            weather_api_url = (
                'https://api.openweathermap.org/data/2.5/weather?units=metric'
                f'&lat={lat}'
                f'&lon={lon}'
                f'&appid={api_key}'

            )
            req_weather = requests.get(weather_api_url)
            if req_weather.status_code == 200:
                data_weather = req_weather.json()
                weather = data_weather['weather'][0]
                main = weather['main']
                description = weather['description']
                temp = data_weather['main']['temp']
                print(f'The weather of {name}:')
                print(f'    Weather: {main}, {description}')
                print(f'    Temperature: {temp}')
