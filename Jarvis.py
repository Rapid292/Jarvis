import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechrecognition
import datetime
import pyaudio # pip install pyaudio
import wikipedia # pip install wikipedia
import webbrowser # pip install webbrowser
import os 
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

emailList = {'Vaibhav':'vaibhav32990@gmail.com', 'Rapid': 'gupta.rishabh2912@gmail.com', 'friend': 'smileshelvi@gmail.com'}

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
        print(hour)

    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am Jarvis sir, Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 500
        print("Listening...")
        r.pause_threshold = 1
        r.operation_timeout = 10
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language="en-in")
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        speak('Please try another query!')
        return 'None'
    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("rapid2912@gmail.com", "Bitcoin29*6")
    server.sendmail("rapid2912@gmail.com", to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            print("Rishabh sir, according to wikipedia...")
            speak("Rishabh sir, according to wikipedia...")
            print(results)
            speak(results)
        
        elif 'hello jarvis' in query:
            speak('hello sir, how may i help you')

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'latest news' in query:
            webbrowser.open('economictimes.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\RAPID\\Desktop\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'a movie' in query:
            movies_dir = 'C:\\Users\\RAPID\\Desktop\\D\\Movies'
            movies = os.listdir(movies_dir)
            os.startfile(os.path.join(movies_dir, random.choice(movies)))

        elif 'game of throne' in query:
            got_dir = 'C:\\Users\\RAPID\\Desktop\\D\\Movies\\Game of Thrones'
            got = os.listdir(got_dir)
            os.startfile(os.path.join(got_dir, got[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"the time is:{strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "C:\\Users\\RAPID\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak('to whom you want to send the mail?')
                reciever = takeCommand()
                to = emailList[reciever]
                speak('What should I say?')
                content = takeCommand()
                sendEmail(to, content)
                speak('email has been sent')
                print(f"Email has been sent to {to}")   
            except Exception as e:
                print(e)
                speak('Sorry sir, Unable to send the email')

        
