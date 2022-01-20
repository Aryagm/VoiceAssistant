import speech_recognition as sr
from playsound import playsound
import setup
from speech import speak

#The introduction statement
intro = setup.introduction

def listen_0():
    """The initial listening, if the the wake_word is found then activate the bot"""
    r = sr.Recognizer()
    while True:
        with sr.Microphone(2) as source:
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
    """The function to take the command from the user"""
    r = sr.Recognizer()
    while True:
        with sr.Microphone(2) as source:
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
    """Understanding the email recipients from user speech"""
    r = sr.Recognizer()
    while True:
        with sr.Microphone(2) as source:
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
    """Recognizing the email subject from user speech"""
    r = sr.Recognizer()
    while True:
        with sr.Microphone(2) as source:
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
    """Recognizing the email body from user speech"""
    r = sr.Recognizer()
    while True:
        with sr.Microphone(2) as source:
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
    """Recognizing the email confirmation from user speech"""
    r = sr.Recognizer()
    while True:
        with sr.Microphone(2) as source:
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
    """Recognizing the youtube video name from user speech"""
    r = sr.Recognizer()
    while True:
        with sr.Microphone(2) as source:
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
