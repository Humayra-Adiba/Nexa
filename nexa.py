import os
import platform
import sys
import subprocess
import speech_recognition
from gtts import gTTS
import tempfile
import platform
import subprocess
import pyautogui
import datetime
from search import searchGoogle
from search import searchYoutube
from search import searchWikipedia
from launchapp import openappweb
from launchapp import closeappweb
from launchapp import minimizeapp

  
# Suppress warnings and sound errors
os.environ["ALSA_LOG_LEVEL"] = "none"
os.environ["PYTHONWARNINGS"] = "ignore"
sys.stderr = open(os.devnull, "w")

def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            temp_path = fp.name
        tts.save(temp_path)
        if platform.system() == "Windows":
            # On Windows, use mpg123 or the default player
            try:
                os.system(f'start /min mpg123 "{temp_path}"')
            except Exception:
                os.system(f'start wmplayer "{temp_path}"')
        else:
            # On Linux, use mpg123
            subprocess.run(["mpg123", temp_path])
        os.remove(temp_path)
    except Exception as e:
        print("[TTS ERROR]", e)
        print(f"Speaking (fallback): {text}")



def takeCommand():
    r = speech_recognition.Recognizer()
    try:
        with speech_recognition.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            try:
                audio = r.listen(source, timeout=4, phrase_time_limit=7)
            except Exception as e:
                print(f"Microphone/audio error: {e}")
                return "None"
    except Exception as e:
        print(f"Microphone not found or not accessible: {e}")
        return "None"

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-US')
        print(f"You Said: {query}\n")
    except Exception as e:
        print(f"Say that again ({e})")
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            try:
                from greet import greetMe
                greetMe()
            except ImportError:
                speak("Greeting module not found. Please make sure it is in the same directory.")

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, you can call me anytime.")
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("That's great, sir. Do you need any help?")
                elif "i am good" in query:
                    speak("That's great, sir. Do you need any help?")
                elif "i am well" in query:
                    speak("That's great, sir. Do you need any help?")
                elif "how are you" in query:
                    speak("i am doing well, sir")
                elif "thank you" in query:
                    speak("You are welcome, sir")
                elif "what is your name" in query:
                    speak("I am Nexa, your Personal Desktop Voice Assistant")
                elif "what can you do" in query:
                    speak("I can do many things,sir.I can help to navigate your PC.I can open applications, search on the web, and much more.")
                elif "who are you" in query:
                    speak("I am Nexa, your Personal Desktop Voice Assistant ")
                elif "can you tell me a joke" in query:
                    speak("Why don't scientists trust atoms? Because they make up everything.")
                elif "who made you" in query:
                    speak("I was made by Humayra, a passionate crazy developer.")
                elif "who created you" in query:
                    speak("I was created by Humayra, a passionate crazy developer.")
                elif "what is your purpose" in query:
                    speak("I am here to help you, sir. I can perform many tasks for you.")
                elif "what is your favorite color" in query:
                    speak("I don't have a favorite color, sir. But I can help you find information about colors.")
                elif "what is your age" in query:
                    speak("I am a computer program, so I don't have an age, sir.")
                elif "how old are you" in query:
                    speak("I am a computer program, so I don't have an age, sir.")
                elif "what is your gender" in query:
                    speak("I am a computer program, so I don't have a gender, sir.")
                elif"are you a artificial intelligence" in query:
                    speak("no,Sir.I am a computer program.")
                elif"are you a human" in query:
                    speak("no,Sir.I am a computer program.")
                elif"are you an ai" in query:
                    speak("no,Sir.I am a computer program.")
                elif"are you a robot" in query:
                    speak("no,Sir.I am a computer program.")
                elif"do you have a crush" in query:
                    speak("Yes,Sir.I have crush on shihab.")
                elif "do you wanna marry someone" in query:
                    speak("Yes,Sir.I wanna marry shihab.")

                #searching from google,youtube,wikipedia
                elif "search google about" in query:
                    searchGoogle(query)
                elif "search youtube about" in query:
                    searchYoutube(query)
                elif"play a song" in query:
                    searchYoutube(query)
                elif "tell me about" in query:
                    searchWikipedia(query)

                #Launch app or website
                elif "open" in query:
                    openappweb(query)
                elif "close" in query:
                    closeappweb(query)
                elif "minimize" in query:
                    minimizeapp(query)


                #Youtube control
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                #Volume control
                elif "volume up" in query:
                    speak("turning the volume up, Sir")
                    volumeup()
                elif "volume down" in query:
                    speak("turning the volume down, Sir")
                    volumedown()

                #Time
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")    

                #exit
                elif "finally sleep" in query:
                    speak("going to sleep, sir. If you need anything, you can wake me up anytime.")
                    exit()
                
                