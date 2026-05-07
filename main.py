import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import io
import wave

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    fs = 16000
    seconds = 4
    
    print("Sun raha hu... bolo")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("Process kar raha hu...")
    
    byte_io = io.BytesIO()
    with wave.open(byte_io, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(recording.tobytes())
    
    byte_io.seek(0)
    r = sr.Recognizer()
    with sr.AudioFile(byte_io) as source:
        audio = r.record(source)
    
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"Tumne bola: {query}")
        return query.lower()
    except:
        return ""

speak("Namaste, main tumhara voice assistant hu")

while True:
    command = listen()
    
    if command == "":
        speak("Samajh nahi aaya, phir se bolo")
        continue

    if "youtube" in command:
        speak("YouTube khol raha hu")
        webbrowser.open("https://youtube.com")
    
    elif "time" in command or "samay" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Abhi {time} baj rahe hain")
    
    elif "google" in command:
        speak("Google khol raha hu")
        webbrowser.open("https://google.com")
    
    elif "band karo" in command or "bye" in command or "exit" in command:
        speak("Theek hai, bye bye")
        break
    
    else:
        speak("Ye command main abhi nahi janta")