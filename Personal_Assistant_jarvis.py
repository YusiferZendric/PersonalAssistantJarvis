import pyttsx3 #pip install pyttsx3
import speech_recognition as sr
import time
#pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

import smtplib
import random
import pyautogui as pt
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'from youtube' in query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[random.randint(0, 9)]))

        elif 'current time' in query or 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'sst folder' in query:
            speak("opening social studies folder")
            

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)

                speak("Sorry my friend harry bhai. I am not able to send this email")
        elif "who is" in query:
            try:
                query.replace("who is", "", 0)
                speak(wikipedia.summary(query))
            except:
                speak("i don't know")
        elif "typing test" in query:
            webbrowser.open("https://10ff.net")
        elif "zoom meeting" in query or "zoom class" in query or "online class" in query:
            os.startfile('C:\\Users\\adity\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
            while True:
                time.sleep(10)
                Join_button_location = pt.locateOnScreen("joinbutton.png", confidence=.6)
                pt.moveTo(Join_button_location)
                pt.click()
                speak("Please tell your meeting id!!")
                meeting_id = takeCommand().lower()
                time.sleep(2)
                entrybox = pt.locateOnScreen("entrybox.png", confidence=.6)
                pt.moveTo(entrybox)
                pt.click()
                pt.typewrite(meeting_id)
                join = pt.locateOnScreen('join.png', confidence=.6)
                pt.moveTo(join)
                pt.click()
                speak("i have started your meeeting!!")
                break


        elif "exit" in query:
            exit()
        else:
            try:
                if query is not None:
                    webbrowser.open(f"https://www.google.com/search?q={query}")
                elif query=="none":
                    speak("i am not able to judge what you have spoken!!")
            except:
                speak("i don't have any information about this topic")