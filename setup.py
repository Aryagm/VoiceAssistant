"""
This is a setup file. Changing the variables below will change the properties of the voice assistant.
The variables are self explanatory.
"""


bot_name = 'Jarvis'

bot_gender = 'Male'

user_name = 'Arya'

introduction = f"Hello {user_name}, how may I help you?"

#email contacts
email_contacts = {'denton': '710068@pdsb.net', "peter": "980078@pdsb.net"}




#################################################################################




email = True
email_intent = ['send an email', 'compose an email', 'write an email',
                'send a email', 'compose a email', 'write a email', 'email']

reminder = True
reminder_intent = ['set a reminder', 'add a reminder']

youtube = True
youtube_intent = ['play','youtube','Play','YouTube','Youtube']

weather = True
weather_intent = ['tell me the weather', 'what is the weather', 'what is the tempreature', 'what is the weather', 'tell the weather', 'tell about the weather',"what's the weather", 'how is the weather', 'what is the tempreature', 'how hot is it', 'how cold is it', 'how is the tempreature', 'when is sunset', 'when is sunrise', 'what is the wind speed', 'what does it feel like', 'what is the maximum tempreature', 'what is the minimum tempreature', 'what is the higest tempreature', 'what is the lowest tempreature', 'show me the weather']

weather_location = True
weather_location_intent = ['tell me the weather in', 'what is the weather in', 'what is the tempreature in', 'what is the weather in', 'tell the weather in', 'tell about the weather in', "what's the weather in", 'how is the weather in', 'what is the tempreature in', 'how hot is it in',
                           'how cold is it in', 'how is the tempreature in', 'when is sunset in', 'when is sunrise in', 'what is the wind speed in', 'what does it feel like in', 'what is the maximum tempreature in', 'what is the minimum tempreature in', 'what is the higest tempreature in', 'what is the lowest tempreature in']


math = True
math_intent = ['solve', 'calculate']

wiki = True
wiki_intent = ['who is', 'where is', 'tell me about', 'tell me who is', 'tell me where is']

date = True
date_intent = ['date','what is the date', 'what date is it', 'what is todays date','what is todays date','tell me todays date', 'tell me the date', "what's the date", "what's todays date", "what's today's date"]

time = True
time_intent = ['time','what is the time', 'what time is it', 'tell me the time', "what's the time"]

affirm_intent = ['yes','sure','go ahead', 'yupp', 'yup','yeah','ok','sounds good']
deny_intent = ['no', 'quit', 'exit',"don't", 'stop', 'delete']
stop_intent = ['terminate','quit','stop']

weather_api = "3a550d5ed6a16a58b286163164ece3fb"

wake_word = bot_name