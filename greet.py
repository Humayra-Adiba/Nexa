from gtts import gTTS
import datetime
import tempfile
import os
import platform
import subprocess

def speak(audio):
    try:
        tts = gTTS(text=audio, lang='en', slow=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            temp_path = fp.name
        tts.save(temp_path)

        if platform.system() == "Windows":
            # Use default player silently
            os.system(f'start /min wmplayer "{temp_path}"')
        else:
            subprocess.run(["mpg123", temp_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        os.remove(temp_path)
    except Exception as e:
        print("[TTS ERROR]", e)
        print(f"Speaking (fallback): {audio}")

def greetMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour <= 12:
        speak("Good morning, sir.")
    elif 12 < hour <= 18:
        speak("Good afternoon, sir.")
    else:
        speak("Good evening, sir.")

    speak("please tell me, how can I help you?")



