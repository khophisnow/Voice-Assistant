import pyttsx3 as p
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time
import random
import datetime
import calendar


Command = ""
Command = input("""
Hello, CAS7TECH AI ROBOT!!!!!

Turn on CAS7TECH AI ROBOT.
Type "ON" to turn on AI
""" 
"Enter Here: ").lower()


if Command == "on":
    print("Starting Robot...")
    time.sleep(2)
    snow = p.init()
    rate = snow.getProperty("rate")
    snow.setProperty("rate", 130)
    voices = snow.getProperty('voices')
    snow.setProperty('voice', voices[1].id) #for female voice 
    def speak(text): 
        snow.say(text)
        snow.runAndWait()
        
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
          
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source,1.2)
            print("listening....")
            audio = r.listen(source)
        text = " "
        try:
            text = r.recognize_google(audio) 
            print(text)
        except sr.UnknownValueError:
            print("Assistant could not understand the audio")
        except sr.RequestError as ex:
            print("Request Error from Google Speech Recognition" + ex)
       
       
        # for today eg; today is thursday, the 11th of November
        now = datetime.datetime.now()
        date_now = datetime.datetime.today()
        week_now = calendar.day_name[date_now.weekday()]
        now_day = now.day
        month_now = now.month 
        year_now = now.year
        month = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",             
        ] 
        ordinals = [
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "6th",
            "7th",
            "8th",
            "9th",
            "10th",
            "11th",
            "12th",
            "13th",
            "14th",
            "15th",
            "16th",
            "17th",
            "18th",
            "19th",
            "20th",
            "21st",
            "22nd",
            "23rd",
            "24th",
            "25th",
            "26th",
            "27th",
            "28th",
            "29th",
            "30th",
            "31st",
        ] 


        if "how are you" in text or "how are you doing" in text:
            speak("I am having a good day sir")
            speak("What can i do for you??")
        elif "fine" in text or "good" in text or "well" in text:
            speak("Alright, that's good to know.")
            speak("What can I do for you?")
        elif "not fine" in text or "not good" in text or "not well" in text or "feeling sick" in text or "feeling ill" in text:
            speak("oh sorry about that.")
            speak(" what can I do for you?")        
        elif "how do you do" in text:
            speak("how do you do sir")
            speak("what can I do for you??")
        elif "what about you" in text or "and you" in text:
            speak("I am having a good day sir")
            speak("What can i do for you??")
        elif 'your name' in text:
            speak("My name is assistant.")
            speak("Anything else that I can do for you?")
        elif 'who created you' in text:
            speak("A technological company in Ghana called CAS7TECH")
            speak("Do you want to know more about my creator?")
            if "yes" in text:
                speak("okay.")
                speak("CAS7TECH COMPANY LIMITED is a technologocal company that deals with...")
            else:
                speak("okay.")
                speak("What else can I do for you?")
        elif 'play' in text:
            song = text.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            exit()
        elif "born" in text:
            speak("I was  born on 1st of November 2022")
        elif "what is" in text or "who is" in text:
            print("searching wikipedia...")
            speak("one sec...")

            search = text.replace('what is','who is' '')
            info = wikipedia.summary(search, 3,3)
            print(info)
            speak(info)
        elif 'time' in text:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('The current time is ' + time)
        elif "can we date" in text:
            speak("I would like to but am already engaged to wifi.")
        elif "today" in text:
            speak("Today is {},{} {}, {}".format(week_now,ordinals[now.day-1],month[now.month-1],year_now))
            print("Today is {},{} {}, {}".format(week_now,ordinals[now.day-1],month[now.month-1],year_now))
        elif 'joke' in text:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
        elif "exit" in text or "quit" in text:
            speak("exitting...in 3")
            speak("2")
            speak("1")
            # time.sleep(1)
            exit()        
        else:
            speak("Please I don't understand what you mean")


elif Command == "off":
    print("shutting down...")
    time.sleep(2)
    print("Shutdown complete!!")
else:
    print("Please Retype Command...") 

