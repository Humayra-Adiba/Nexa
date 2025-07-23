import os
import wolframalpha
from gtts import gTTS
from dotenv import load_dotenv
import re
load_dotenv()

API_KEY = os.getenv("API_KEY")


def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    os.system("mpg123 temp.mp3")  # Use 'mpg123' or 'afplay' on macOS

def WolfRamAlpha(query):
    apikey = API_KEY
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def preprocess_query(query: str) -> str:
    q = query.lower()
    # Remove wake word or assistant name
    q = q.replace("nexa", "").strip()


    replacements = {
        "plus": "+",
        "minus": "-",
        "times": "*",
        "multiply": "*",
        "multiplied by": "*",
        "divide": "/",
        "divided by": "/",
        "over": "/",
        "power": "^",
        "to the power of": "^",
        "squared": "^2",
        "cubed": "^3",
        "sine": "sin",
        "cosine": "cos",
        "tangent": "tan",
    }

    for phrase, symbol in replacements.items():
        # word boundaries ensure full-word matches only
        q = re.sub(rf"\\b{phrase}\\b", symbol, q)

    # condense whitespace
    q = re.sub(r"\s+", " ", q).strip()
    return q


def Calc(query):
    processed_query = preprocess_query(str(query))
    try:
        result = WolfRamAlpha(processed_query)
        if result:
            print(result)
            speak(result)
        else:
            speak("I couldn't get an answer from Wolfram Alpha.")
    except Exception as e:
        print(f"Calculation error: {e}")
        speak("Sorry, I couldn't calculate that.")
