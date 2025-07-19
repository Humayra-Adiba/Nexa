import os
import pyautogui
import webbrowser
from time import sleep
from gtts import gTTS
from playsound import playsound
import platform

# Detect OS
is_linux = platform.system() == "Linux"

# gTTS speak function
def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("voice.mp3")
    playsound("voice.mp3")
    os.remove("voice.mp3")

# App dictionary (cross-platform)
dictapp = {
    "commandprompt": "gnome-terminal" if is_linux else "cmd",
    "paint": "gimp" if is_linux else "paint",
    "word": "libreoffice --writer" if is_linux else "winword",
    "excel": "libreoffice --calc" if is_linux else "excel",
    "chrome": "google-chrome" if is_linux else "chrome",
    "vscode": "code",
    "powerpoint": "libreoffice --impress" if is_linux else "powerpnt",
    "discord": "discord"
}

# Open app or website
def openappweb(query):
    speak("Launching, sir.")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "").replace("nexa", "").replace("launch", "").replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        for app in dictapp:
            if app in query:
                command = dictapp[app]
                if is_linux:
                    os.system(f"{command} &")  # launch in background
                else:
                    os.system(f"start {command}")
                break

# Close apps or browser tabs
def closeappweb(query):
    speak("Closing, sir.")
    if "tab" in query:
        num = sum(char.isdigit() for char in query)
        for _ in range(num or 1):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)
        speak("All tabs closed.")
    else:
        for app in dictapp:
            if app in query:
                process = dictapp[app].split()[0]
                if is_linux:
                    os.system(f"pkill {process}")
                else:
                    os.system(f"taskkill /f /im {process}.exe")
                break

# Minimize windows
def minimizeapp(query):
    speak("Minimizing, sir.")
    if is_linux:
        # Requires: sudo apt install wmctrl
        os.system("wmctrl -k on")
    else:
        pyautogui.hotkey("win", "down")
