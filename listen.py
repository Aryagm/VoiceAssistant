import speech_recognition as sr
from playsound import playsound
import setup
from speech import speak

#The introduction statement
intro = setup.introduction

def listen_0():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Ready...")
            try:
                audio = r.listen(source)

                query = r.recognize_google(audio)
                print(query)
                if query.find(setup.wake_word) >= 0 or query.find(setup.wake_word.lower()) >= 0:
                    speak(intro)
                    break
            except:
                pass
    return query


def take_command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            playsound('ding.mp3')
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            speak('Just give me a second')
        except:
            print("There was an error processing the request, please try again.")
            speak("There was an error processing the request, please try again.")
            continue
        return query


def email_recipients():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            playsound('ding.mp3')
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            speak('Checking your contacts')
        except:
            print(
                "I couldn't recognise the recipients. Could you please repeat their names?")
            speak(
                "I couldn't recognise the recipients. Could you please repeat their names")

            continue
        return query


def email_sub():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            playsound('ding.mp3')
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            speak('Adding the Subject...')
        except:
            print("I could not listen to the subject. Could you please repeat it?")
            speak("I could not listen to the subject. Could you please repeat it?")
            continue
        return query


def email_body():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            playsound('ding.mp3')
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            speak('Composing the body...')
        except:
            print("I could recognise the text in the body. Could you please repeat it?")
            speak("I could recognise the text in the body. Could you please repeat it?")
            continue
        return query


def email_confirm():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            playsound('ding.mp3')
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            speak('Processing your request...')
        except:
            print("I couldn't hear you. Please repeat your confirmation.")
            speak("I couldn't hear you. Please repeat your confirmation.")
            continue
        return query


def youtube_listen():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            playsound('ding.mp3')
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            speak('Processing your request...')
        except:
            print("I couldn't hear you. Could you please repeat?")
            speak("I couldn't hear you. Could you please repeat?")
            continue
        return query
