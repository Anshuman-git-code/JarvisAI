import speech_recognition as sr
import os
import webbrowser
import datetime
import time

def say(text):
    os.system(f"say {text}")
    time.sleep(1)  

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print(f"Error: {e}")
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Pycharm')
    say("Hello, I am Jarvis A.I.")
    while True:
        print("Listening...")
        query = takeCommand().lower()

        if "stop Jarvis" in query:
            say("Shutting down.")
            break

        # Open Websites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ["instagram", "https://www.instagram.com"]]
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]} ")
                webbrowser.open(site[1])

        # Search the Web
        if "search" in query:
            query = query.replace("search", "")
            say(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        # Open Applications 
        if "open calculator" in query:
            say("Opening Calculator")
            os.system("open /System/Applications/Calculator.app")

        if "open notes" in query:
            say("Opening Notes")
            os.system("open /System/Applications/Notes.app")

        # Check the Weather
        if "weather" in query:
            say("Checking the weather")
            webbrowser.open("https://weather.com/en-IN/weather/today/l/20.25,85.80?par=google")

        # Set a Reminder
        if "set a reminder" in query:
            say("What should I remind you about?")
            reminder = takeCommand().lower()
            say(f"Reminder set for: {reminder}")
            with open("reminders.txt", "a") as f:
                f.write(f"Reminder: {reminder}\n")

        # Tell the Time
        if "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strTime}")


        # Open Email
        if "open email" in query:
            say("Opening Gmail")
            webbrowser.open("https://mail.google.com/")

        # Check News
        if "news" in query:
            say("Fetching the latest news")
            webbrowser.open("https://news.google.com/")

        # Turn Off the System
        if "shutdown" in query:
            say("Shutting down the system")
            os.system("shutdown now")


        # Open Music File 
        if "open music" in query:
            musicPath = "/Users/anshumanmohapatra/Downloads/T20IFinalBass.mp3"
            os.system(f"open {musicPath}")
