import speech_recognition as sr
import pyttsx3

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            return "Sorry, I didn't catch that."

def speak_response(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()