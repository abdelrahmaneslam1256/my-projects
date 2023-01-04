import pyttsx3
import speech_recognition as sr
import wikipedia 
import webbrowser
import os

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[0].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.run()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query


if __name__ == '__main__':

    speak("hello there ")
    speak("how can i help you")
    while True:
        query = take_command().lower()
        if "let's play"and " memory game" in query:
            speak("lets play")

