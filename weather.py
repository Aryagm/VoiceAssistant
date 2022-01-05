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
    """Recognises the name of the city from the user's speech"""
    
    # Initializing the speech to text engine:
    r = sr.Recognizer()
    
    while True:
        
        # Listening to the user:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            playsound('ding.mp3')
            audio = r.listen(source)
       
        try:
            print("Recognizing...")
            # Converting the audio to text:
            query = r.recognize_google(audio, language='en-CA')
            speak('Processing your request...')
        except:
            # Print an error if the above process errors out:
            print("I couldn't hear you. Please repeat the name of the city.")
            speak("I couldn't hear you. Please repeat the name of the city.")
            continue
        return query

def city_weather(city):
    """Gets the weather for that city from the weather api and outputs it as speech"""
    
    # Fetching the weather details from the api:
    api_key = setup.weather_api
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    
    # Getting the weather details from the json file:
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
    
    # Printing out the details:
    print("Location: "+location)
    print("Tempreature: "+tempreature)
    print("Description: "+description)
    print("Feels Like: "+feel)
    print("Wind Speed: "+wind_speed)
    print("Minimum Tempreature: "+min_temp)
    print("Maximum Tempreature: "+max_temp)
    print("Todays Sunrise: "+sunrise)
    print("Todays Sunset: "+sunset)
    
    # Creating the final statement:
    statement = "In "+city+" , "+"The temperature is "+tempreature+", "+"It feels like "+feel+". "+"The forecast is "+description+". "+"The wind speed is " + \
        wind_speed+". "+"The minimum temperature is "+min_temp+" and the maximum temperature is " + \
        max_temp+". "+"Todays sunrise: "+sunrise+", and todays sunset: "+sunset
    
    # Converting the statement to text:
    speak(statement)

def user_weather():
    """Gets the location of the user based on the ip address and returns the weather for that place"""
    
    # Getting the location:
    g = geocoder.ip('me')
    latitude = g.lat
    longitude = g.lng
    
    # Fetching the weather details from the api:
    api_key = setup.weather_api
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + "lat=" + \
        str(latitude) + "&lon=" + str(longitude) + "&appid=" + api_key
    response = requests.get(complete_url)
    x = response.json()
    
    # Getting the weather details from the json file:
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
    
    # Printing out the details:
    print("Location: "+location)
    print("Tempreature: "+tempreature)
    print("Description: "+description)
    print("Feels Like: "+feel)
    print("Minimum Tempreature: "+min_temp)
    print("Maximum Tempreature: "+max_temp)
    print("Todays Sunrise: "+sunrise)
    print("Todays Sunset: "+sunset)
    
    # Creating the final statement:
    statement = "In "+location+" , "+"The temperature is "+tempreature+", "+"It feels like "+feel+". "+"The forecast is "+description+". "+"The wind speed is " + \
        wind_speed+". "+"The minimum temperature is "+min_temp+" and the maximum temperature is " + \
        max_temp+". "+"Todays sunrise: "+sunrise+", and todays sunset: "+sunset
   
    # Converting the statement to text:
    speak(statement)



