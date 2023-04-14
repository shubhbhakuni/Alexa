import pyttsx3
import datetime as dt
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices' , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Himanshu!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Himanshu!")
    else:
        speak("Good Evening Himanshu!")
    speak("I am at your service . How may I help you sir")

def takecommand():
    #it takes command from user end through microphone and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio , language='en-in')
        print("User said: ",query)

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    if 1:
        query = takecommand().lower()
        
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query , sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif "google" in query:
            webbrowser.open("google.com")
        elif "stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir , songs[random.randint(0,6)]))
        elif "time" in query:
            strTime = dt.datetime.now().strftime("%I:%M:%S %p")
            speak(f"Sir , the current time is {strTime}")
        elif 'open vs code' in query:
            codePath = "C:\\Users\\HP WORLD\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "play movies" in query:
            movies_dir = 'E:\\Movies'
            movies = os.listdir(movies_dir)
            os.startfile(os.path.join(movies_dir , movies[random.randint(0,5)]))
        elif "on youtube" in query:
            speak("Playing")
            query = query.replace("on youtube","")
            pywhatkit.playonyt(query)
        elif "jokes" in query:
            speak(pyjokes.get_joke())
        elif "bored" in query:
            speak("How can I cheer you up ")
            speak("shall I play some music on youtube or movies or you wanna hear some jokes")
            query = takecommand().lower()
            if "play music" in query:
                music_dir = 'E:\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir , songs[random.randint(0,6)]))
            elif "play movies" in query:
                movies_dir = 'E:\\Movies'
                movies = os.listdir(movies_dir)
                os.startfile(os.path.join(movies_dir , movies[random.randint(0,1)]))
            elif "on youtube" in query:
                speak("Playing")
                query = query.replace("on youtube","")
                pywhatkit.playonyt(query)
            elif "jokes" in query:
                speak(pyjokes.get_joke())