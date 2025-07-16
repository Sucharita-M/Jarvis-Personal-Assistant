import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import time


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 170)

def speak(audio):
    print("Jarvis:", audio)
    engine.say(audio)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. Your personal assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said:", query)
        return query.lower()
    except Exception as e:
        speak("Sorry, I didn't understand. Can you repeat?")
        return ""

def execute_command(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia...")
        speak(result)

    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif 'open stack overflow' in query:
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")

    elif 'play music' in query:
        music_dir = "C:\\Users\\Public\\Music\\Sample Music" 
        songs = os.listdir(music_dir)
        if songs:
            song = random.choice(songs)
            os.startfile(os.path.join(music_dir, song))
        else:
            speak("No music files found.")

    elif 'time' in query:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {str_time}")

    elif 'open code' in query:
        code_path = "C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)

    elif 'joke' in query:
        jokes = [
            "Why did the computer go to therapy? It had too many bytes of trauma.",
            "What do you call a group of musical whales? An orca-stra.",
            "Why do Java developers wear glasses? Because they don't see sharp."
        ]
        speak(random.choice(jokes))

    elif 'your name' in query or 'who are you' in query:
        speak("I am Jarvis, your virtual voice assistant.")

    elif 'sleep' in query or 'stop listening' in query:
        speak("Okay, I will sleep now. Say 'wake up Jarvis' when you need me again.")
        return 'sleep'

    elif 'exit' in query or 'shutdown' in query or 'bye' in query:
        speak("Goodbye! Have a nice day.")
        exit()

    else:
        speak("Sorry, I can't do that yet.")

def jarvis_loop():
    wish_user()
    active = True

    while True:
        if active:
            query = take_command()
            if 'sleep' in query or 'stop listening' in query:
                active = False
                speak("Going to sleep mode. Say 'wake up Jarvis' to reactivate.")
            else:
                if query != "":
                    status = execute_command(query)
                    if status == 'sleep':
                        active = False
        else:
            query = take_command()
            if 'wake up jarvis' in query or 'wake up' in query:
                active = True
                speak("I am back. How can I help you?")


jarvis_loop()
