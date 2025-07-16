import os
import platform
import sys
import subprocess
import speech_recognition


# Suppress warnings and sound errors
os.environ["ALSA_LOG_LEVEL"] = "none"
os.environ["PYTHONWARNINGS"] = "ignore"
sys.stderr = open(os.devnull, "w")

def speak(text):
    """
    Speaks the given text using gTTS (Google Text-to-Speech).
    Requires: pip install gtts
    Also requires: sudo apt install mpg123 (Linux) or install mpg123 for Windows.
    """
    from gtts import gTTS
    import tempfile
    import platform
    import os
    import subprocess
    import sys
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
