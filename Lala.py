import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

print("initializing Lala")

MASTER = "simon"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


# speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
        speak("")

# microphone


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said: {query}\n")
        speak(f"user said: {query}\n")

    except Exception as _:
        print("say that again please")
        query = None

    return query


# main start here
print("Hello my name is Lala, i can help you!")
speak("Hello my name is Lala, i can help you!")
wishMe()
query = takeCommand()

# system logic for task as per query
if "wikipedia" in query.lower():
    speak("searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

elif "open youtube" in query.lower():
    url = "youtube.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif "open google" in query.lower():
    url = "google.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif "play music" in query.lower():
    print("Wait I will play music")
    speak("Wait I will play music")
    songs_dir = "D:/Belajar/Python/music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))

elif "the time" in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print(strTime)
    speak(f"{MASTER} the time is {strTime}")
