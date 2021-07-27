bot_name = 'Jarvis'

bot_gender = 'Male'

user_name = 'Arya'

wake_word = 'Jarvis'

introduction = f"Hello {user_name}, how may I help you?"

email = True
email_intent = ['send an email', 'compose an email', 'write an email',
                'send a email', 'compose a email', 'write a email']

reminder = True
reminder_intent = ['set a reminder', 'add a reminder']

youtube = True
youtube_intent = ['play','youtube','Play','YouTube','Youtube']

weather = True
weather_intent = ['tell me the weather', 'what is the weather', 'what is the tempreature', 'what is the weather', 'tell the weather', 'tell about the weather',"what's the weather", 'how is the weather', 'what is the tempreature', 'how hot is it', 'how cold is it', 'how is the tempreature', 'when is sunset', 'when is sunrise', 'what is the wind speed', 'what does it feel like', 'what is the maximum tempreature', 'what is the minimum tempreature', 'what is the higest tempreature', 'what is the lowest tempreature']

weather_location = True
weather_location_intent = ['tell me the weather in', 'what is the weather in', 'what is the tempreature in', 'what is the weather in', 'tell the weather in', 'tell about the weather in', "what's the weather in", 'how is the weather in', 'what is the tempreature in', 'how hot is it in',
                           'how cold is it in', 'how is the tempreature in', 'when is sunset in', 'when is sunrise in', 'what is the wind speed in', 'what does it feel like in', 'what is the maximum tempreature in', 'what is the minimum tempreature in', 'what is the higest tempreature in', 'what is the lowest tempreature in']


math = True
math_intent = ['solve', 'calculate']

wiki = True
wiki_intent = ['who is', 'where is', 'tell me about', 'tell me who is', 'tell me where is']

date = True
date_intent = ['what is the date', 'what date is it', 'what is todays date','tell me todays date', 'tell me the date', "what's the date", "what's todays date"]

time = True
time_intent = ['what is the time', 'what time is it', 'tell me the time', "what's the time"]

affirm_intent = ['yes','sure','go ahead', 'yupp', 'yup','yeah','ok','sounds good']
deny_intent = ['no', 'quit', 'exit',"don't", 'stop', 'delete']
stop_intent = ['terminate','quit','stop']

#email contacts
email_contacts = {'mom': 'email@server.com', 'dad': 'email@server.com', 'myself': 'email@server.com'}

weather_api = "API_KEY from https://openweathermap.org/price"

