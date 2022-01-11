import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from random import choice
from utils import opening_text
from functions.online_ops import find_my_ip, get_random_joke, play_on_youtube, search_on_google, search_on_wikipedia
from functions.os_ops import open_calculator, open_notepad
from pprint import pprint


USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 190)

engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greets the user according to the time"""

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")

def take_user_input():
    """Takes user input, recogniyes it using Speech Recognition module and coverts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-US')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()
        elif 'open calculator' in query:
            open_calculator()
        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)