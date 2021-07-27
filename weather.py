import os
from datetime import datetime
import geocoder
import pafy
import pyttsx3
import requests
import speech_recognition as sr
import wikipediaapi
from playsound import playsound
from win32com import client
from youtube_search import YoutubeSearch
import setup
from speech import speak

def weather_loc():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            playsound('ding.mp3')
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-CA')
            speak('Processing your request...')
        except:
            print("I couldn't hear you. Please repeat the name of the city.")
            speak("I couldn't hear you. Please repeat the name of the city.")
            continue
        return query

def city_weather(city):
    api_key = setup.weather_api
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    location = x['name']
    description = x['weather'][0]['description']
    tempreature = str(round(x['main']['temp'] - 273.15, 2)) + "°C"
    feel = str(round(x['main']['feels_like'] - 273.15, 2)) + "°C"
    wind_speed = str(round(x['wind']['speed'] * 3.6, 2)) + " kph"
    min_temp = str(round(x['main']['temp_min'] - 273.15, 2)) + "°C"
    max_temp = str(round(x['main']['temp_max'] - 273.15, 2)) + "°C"
    sunrise = str(datetime.fromtimestamp(
        x['sys']['sunrise']).strftime('%I:%M %p'))
    sunset = str(datetime.fromtimestamp(
        x['sys']['sunset']).strftime('%I:%M %p'))
    print("Location: "+location)
    print("Tempreature: "+tempreature)
    print("Description: "+description)
    print("Feels Like: "+feel)
    print("Wind Speed: "+wind_speed)
    print("Minimum Tempreature: "+min_temp)
    print("Maximum Tempreature: "+max_temp)
    print("Todays Sunrise: "+sunrise)
    print("Todays Sunset: "+sunset)
    statement = "In "+city+" , "+"The temperature is "+tempreature+", "+"It feels like "+feel+". "+"The forecast is "+description+". "+"The wind speed is " + \
        wind_speed+". "+"The minimum temperature is "+min_temp+" and the maximum temperature is " + \
        max_temp+". "+"Todays sunrise: "+sunrise+", and todays sunset: "+sunset
    speak(statement)

def user_weather():
    g = geocoder.ip('me')
    latitude = g.lat
    longitude = g.lng
    api_key = setup.weather_api
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + "lat=" + \
        str(latitude) + "&lon=" + str(longitude) + "&appid=" + api_key
    response = requests.get(complete_url)
    x = response.json()
    location = x['name']
    description = x['weather'][0]['description']
    tempreature = str(round(x['main']['temp'] - 273.15, 2)) + "°C"
    feel = str(round(x['main']['feels_like'] - 273.15, 2)) + "°C"
    wind_speed = str(round(x['wind']['speed'] * 3.6, 2)) + " kph"
    min_temp = str(round(x['main']['temp_min'] - 273.15, 2)) + "°C"
    max_temp = str(round(x['main']['temp_max'] - 273.15, 2)) + "°C"
    sunrise = str(datetime.fromtimestamp(
        x['sys']['sunrise']).strftime('%I:%M %p'))
    sunset = str(datetime.fromtimestamp(
        x['sys']['sunset']).strftime('%I:%M %p'))
    print("Location: "+location)
    print("Tempreature: "+tempreature)
    print("Description: "+description)
    print("Feels Like: "+feel)
    print("Minimum Tempreature: "+min_temp)
    print("Maximum Tempreature: "+max_temp)
    print("Todays Sunrise: "+sunrise)
    print("Todays Sunset: "+sunset)
    statement = "In "+location+" , "+"The temperature is "+tempreature+", "+"It feels like "+feel+". "+"The forecast is "+description+". "+"The wind speed is " + \
        wind_speed+". "+"The minimum temperature is "+min_temp+" and the maximum temperature is " + \
        max_temp+". "+"Todays sunrise: "+sunrise+", and todays sunset: "+sunset
    speak(statement)



