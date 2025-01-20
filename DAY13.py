#!/usr/bin/env python3
import requests

api_key ="f8b68d2e67ea0d9c8d52f0403f497830"

def get_weather(city):
    weather =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    responds = requests.get(weather)
    data =responds.json()
    print(data)


    # Displaying weather Info
    print("\nHere is your weather info: \n")
    print(f"Weather: {data['weather'][0]['main']}")
    print(f"Description: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}")
    print(f"Humidity: {data['main']['humidity']}")
    print(f"Wind Speed: {data['wind']['speed']}")
    print(f"The country of your city is {data['sys']['country']}")


city = input("Enter a city \n")


get_weather(city)