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
import listen
import weather
from speech import speak
import speech
import re
import nltk
from datetime import date


if __name__ == '__main__':
    while True:
        
        # Listening to the user and initializing some variables:
        init = listen.listen_0()
        query = listen.take_command()
        query_lower = query.lower()
        terminate = False
        email = False
        yt = False
        weather_bool = False
        weather_bool_loc = False
        time = False
        date1 = False
        wikipedia = False
        math = False
        
        # Checking for the intent and stop the program if exit intent is True:
        for x in setup.stop_intent:
            if x == query_lower:
                print("terminate")
                terminate = True
                break
        if terminate == True:
            speak("Process terminated. Goodbye! ")
            break    
        print(query)
        
        # Check if user wants to send email and if True send the email:
        for x in setup.email_intent:
            if x in query and setup.email==True:
                speak("Whom do you want to send an email to?")
                recipients = listen.email_recipients()
                recipients = recipients.lower()
                for x in setup.stop_intent:
                    if x == recipients:
                        print("terminate")
                        terminate = True
                        break
                if terminate == True:
                    speak("Process terminated. Goodbye! ")
                    break
                print(recipients)
                recipients = recipients.split()
                if 'and' in recipients:
                    recipients.remove('and')
                print(recipients)
                remove_lst = []
                for x in recipients:
                    print(x)
                    if x not in setup.email_contacts.keys():
                        print(x)
                        sentence = x + " is not found in your contacts! " + \
                            x + " will not receive an email."
                        speak(sentence)
                        print(sentence)
                        remove_lst.append(x)
                for rec in remove_lst:
                    recipients.remove(rec)
                if len(recipients) == 0:
                    print(
                        'No recipients are in your contacts, please try again. Goodbye!')
                    speak(
                        'No recipients are in your contacts, please try again. Goodbye!')
                    break
                if len(recipients) == 1:
                    sentence = "The recipient is "
                elif len(recipients) > 1:
                    sentence = "The recipients are "
                for reci in recipients:
                    sentence = sentence + reci+", "
                speak(sentence)
                print(sentence)
                recipient_emails = []
                for x in recipients:
                    recipient_emails.append(setup.email_contacts[x])
                outlook = client.Dispatch("Outlook.Application")
                message = outlook.CreateItem(0)
                final_recipients = [x + "; " for x in recipient_emails]
                print(final_recipients)
                to = ""
                for x in final_recipients:
                    to = to+x+" "
                print(to)
                message.To = to
                print("What should be the subject of your email?")
                speak("What should be the subject of your email?")
                subject = listen.email_sub()
                for x in setup.stop_intent:
                    if x == subject:
                        print("terminate")
                        terminate = True
                        break
                if terminate == True:
                    speak("Process terminated. Goodbye! ")
                    break
                message.Subject = subject
                print("What should be the body of your email?")
                speak("What should be the body of your email?")
                body = listen.email_body()
                for x in setup.stop_intent:
                    if x == body:
                        print("terminate")
                        terminate = True
                        break
                if terminate == True:
                    speak("Process terminated. Goodbye! ")
                    break
                message.Body = body
                print("Do you want to send the email?")
                print(sentence)
                text_sub = "The subject is: " + subject
                text_body = "The body is: " + body
                print(text_sub)
                print(text_body)
                speech.engine.say(sentence)
                speech.engine.say(text_sub)
                speech.engine.say(text_body)
                speak("Do you want to send the email?")
                confirmation = listen.email_confirm()
                for x in setup.stop_intent:
                    if x == subject:
                        print("terminate")
                        terminate = True
                        break
                if terminate == True:
                    speak("Process terminated. Goodbye! ")
                    break
                for x in setup.affirm_intent:
                    if x in confirmation:
                        message.Send()
                        print("Email sent! You can call me again anytime! Goodbye!")
                        speak("Email sent! You can call me again anytime! Goodbye!")
                        email = True
                        break
                for x in setup.deny_intent:
                    if x in confirmation:
                        message.Delete()
                        print("Email deleted. Goodbye! ")
                        speak("Email deleted. Goodbye! ")
                        email = True
                        break
        
        # Check if user wants to view youtube and if True start the video:
        for x in setup.youtube_intent:
            if x in query and email == False and setup.youtube == True:
                try:
                    inp = query.replace('play', '')
                    inp = inp.replace('Play', '')
                    inp = inp.strip()
                    if len(inp) <= 0:
                        print('What do you want to play?')
                        speak('What do you want to play?')
                        playsound('ding.mp3')
                        inp = listen.youtube_listen()
                    for x in setup.stop_intent:
                        if x == inp:
                            print("terminate")
                            terminate = True
                            break
                    if terminate == True:
                        speak("Process terminated. Goodbye! ")
                        break
                    results = YoutubeSearch(inp, max_results=10).to_dict()
                    url = 'https://www.youtube.com' + results[0]['url_suffix']
                    video = pafy.new(url)
                    best = video.getbest()
                    print(url)
                    os.startfile(best.url)
                    yt = True
                    break
                except:
                    print("There was an error playing the video. Please try again.")
                    speak("There was an error playing the video. Please try again.")
                    break

                    
        # Check if user wants to check the weather_bool of a city and if True send the weather_bool:
        for x in setup.weather_location_intent:
            if x in query and yt == False and setup.weather_location == True:
                city = query.replace(x,"")
                try:
                    if len(city)<=3:
                        print("Of what city do you want the weather?")
                        speak("Of what city do you want the weather?")
                        city = weather.weather_loc()
                        break
                    else:
                        weather.city_weather(city)
                        weather_bool_loc = True
                        break
                    
                except:
                    error_state = "There was an error getting the weather. Please make sure the city you named exists and that you have internet connection."
                    print(error_state)
                    speak(error_state)
                    weather_bool_loc = True
                    break

        # Check if user wants to check the weather_bool of their location and if True send the weather_bool:
        for x in setup.weather_intent:
            if x in query and weather_bool_loc == False and setup.weather == True:
                try:
                    weather.user_weather()
                    weather_bool = True
                    break
                except:
                    print(
                        "There was an error getting the weather. Please make sure you have an internet connection.")
                    speak(
                        "There was an error getting the weather. Please make sure you have an internet connection.")
                    weather_bool = True
                    break

        # Check if user wants to check the time and if True tell the time:
        for x in setup.time_intent:
            if x in query and weather_bool == False and setup.time == True:
                try:
                    time_now = datetime.now()
                    current_time = time_now.strftime("%I:%M %p")
                    time_statement = "Current time is "+current_time
                    print("Current Time:", current_time)
                    speak(time_statement)
                    time = True
                    break
                except:
                    print("There was an error getting the time. Please try again!")
                    speak("There was an error getting the time. Please try again!")
                    time = True
                    break

        # Check if user wants to check the date and if True tell the date:
        for x in setup.date_intent:
            from datetime import date
            if x in query and setup.date == True:
                try:
                    date_today = date.today()
                    date_statement = "Todays date is "+str(date_today)
                    print("Todays Date: ", date_today)
                    speak(date_statement)
                    date1 = True
                    break
                except:
                    print("There was an error getting the date. Please try again!")
                    speak("There was an error getting the date. Please try again!")
                    date1 = True
                    break
        # Check if user wants to get some wiki info and if True find the article:
        for r in range(1):
            if 'what is' in query and date == False and time == False:
                text = query.replace('tell me what is', "")
                text = query.replace('what is ', "")
                text = text.replace("an ", "")
                text = text.replace("a ", "")
                text = text.replace("the ", "")
                if setup.wiki == True:
                    wiki_wiki = wikipediaapi.Wikipedia('en')
                try:
                    if setup.math == True:
                        ans = str(eval(text))
                    ans_state = text + " is equal to "+ans
                    print(ans_state)
                    speak(ans_state)
                    math = True
                    break
                except:
                    #try:
                        ans = text.lower()
                        page = wiki_wiki.page(text)
                        ans = page.text
                        ans = re.sub(r'\[.*?\]+', '', ans)
                        ams = ans.replace('\n', '')
                        ans = ans.replace('\xa0', ' ')
                        ans = re.sub(r"\([^()]*\)", "", ans)
                        a_list = nltk.tokenize.sent_tokenize(ans)
                        a = re.sub(r"\([^()]*\)", "", a_list[0])
                        a_list[0] = a
                        a_list[0] = a_list[0].replace('\n', '')
                        final = a_list[0]+" "+a_list[1]+" "+a_list[2]
                        print(final)
                        speak(final)
                        wikipedia = True
                        break
                    #except:
                    #    print('Article not found. Please try again.')
                    #    speak("Article not found. Please try again.")
                    #    wikipedia = True
                    #    break
                        
        # Check if user wants to get some wiki info and if True find the article:
        for x in setup.wiki_intent:
            if x in query and math == False and wikipedia == False and setup.wiki == True:
                text = query.replace(x, "")
                text = text.replace("an ", "")
                text = text.replace("a ", "")
                text = text.replace("the ", "")
                wiki_wiki = wikipediaapi.Wikipedia('en')
                try:
                    ans = text.lower()
                    page = wiki_wiki.page(text)
                    ans = page.text
                    ans = re.sub(r'\[.*?\]+', '', ans)
                    ams = ans.replace('\n', '')
                    ans = ans.replace('\xa0', ' ')
                    ans = re.sub(r"\([^()]*\)", "", ans)
                    a_list = nltk.tokenize.sent_tokenize(ans)
                    a = re.sub(r"\([^()]*\)", "", a_list[0])
                    a_list[0] = a
                    a_list[0] = a_list[0].replace('\n', '')
                    final = a_list[0]+" "+a_list[1]+" "+a_list[2]
                    print(final)
                    speak(final)
                    wikipedia = True
                    break
                except:
                    print('Article not found. Please try again later.')
                    speak("Article not found. Please try again later.")
                    wikipedia = True
                    break
        
        # Check if user wants to get solve a math problem, if true tell the answer:
        for x in setup.math_intent:
            if x in query and math == False and wikipedia == False and setup.math == True:
                text = query.replace(x, "")
                try:
                    ans = eval(text)
                    ans_state = text + " is equal to "+str(ans)
                    print(ans_state)
                    speak(ans_state)
                    math = True
                    break
                except:
                    error_state = "Unable to solve "+text+". Please try again."
                    print(error_state)
                    speak(error_state)
                    math = True
                    break

         # If the user says something the bot does not understand. Give an error message:
        if yt == False and email == False and weather_bool == False and weather_bool_loc==False and time == False and date1 == False and wikipedia == False and math == False:
            print("I could not understand you, please try calling me again. Goodbye!")
            speak("I could not understand you, please try calling me again. Goodbye!")
            continue
