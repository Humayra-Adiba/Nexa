import speech_recognition
import pywhatkit
import wikipedia
import webbrowser
from gtts import gTTS
import tempfile
import subprocess
import os


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again please.I didn't get that")
        return "None"
    return query.lower()


def speak(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        # Use system audio player
        try:
            subprocess.run(['mpg123', fp.name], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except (subprocess.CalledProcessError, FileNotFoundError):
            try:
                subprocess.run(['paplay', fp.name], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except (subprocess.CalledProcessError, FileNotFoundError):
                try:
                    subprocess.run(['aplay', fp.name], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                except (subprocess.CalledProcessError, FileNotFoundError):
                    print(f"Could not play audio: {text}")
        finally:
            # Clean up the temporary file
            try:
                os.unlink(fp.name)
            except OSError:
                pass


def searchGoogle(query):
    import wikipedia as googleScrap
    query = query.replace("nexa", "")
    query = query.replace("search google about", "")
    query = query.replace("google search", "")
    query = query.replace("google", "")
    query = query.strip()
    speak("This is what I found on Google, Sir")

    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query, 1)
        speak(result)

    except:
        speak("No speakable output available, Sir")


def searchYoutube(query):
    speak("This is what I found for your search on youtube, Sir")
    query = query.replace("search youtube about", "")
    query = query.replace("play a song", "")
    query = query.replace("youtube search", "")
    query = query.replace("youtube", "")
    query = query.replace("nexa", "")
    query = query.strip()
    
    try:
        pywhatkit.playonyt(query)
        speak("Done, Sir")
    except Exception as e:
        speak("Sorry, I couldn't play that on YouTube")


def searchWikipedia(query):
    speak("Searching from Wikipedia...")
    query = query.replace("tell me about", "")
    query = query.replace("wikipedia", "")
    query = query.replace("tell me", "")
    query = query.replace("nexa", "")
    query = query.strip()
    
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia..")
        print(results)
        speak(results)
    except Exception as e:
        speak("Sorry, I couldn't find information about that on Wikipedia")


# Driver Code - Only run if this file is executed directly
if __name__ == "__main__":
    query = takeCommand()
    searchGoogle(query)
    searchYoutube(query)
    searchWikipedia(query)
