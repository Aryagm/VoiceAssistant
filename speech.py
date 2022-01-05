import pyttsx3 as tts
import setup


#Initializing the text-to-speech engine
# It will assign the value as male or female based on setup.py
engine = tts.init('sapi5')
voices = engine.getProperty('voices')
if setup.bot_gender == 'Male':
    engine.setProperty('voice', voices[0].id)
elif setup.bot_gender == 'Female':
    engine.setProperty('voice', voices[1].id)

#The function to say things
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
