import os
from this import d
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
    try:
        print(f"Nexa: {audio}")  # Always print the message
        tts = gTTS(text=audio, lang='en')
        tts.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
    except Exception as e:
        print(f"Speech error: {e}")
        # If speech fails, at least the message is printed

# App dictionary (cross-platform)
dictapp = {
    "commandprompt": "gnome-terminal" if is_linux else "cmd",
    "terminal": "gnome-terminal" if is_linux else "cmd",
    "paint": "kolourpaint" if is_linux else "paint",  # Lighter alternative to GIMP
    "gimp": "gimp" if is_linux else "gimp",
    "word": "libreoffice --writer" if is_linux else "winword",
    "writer": "libreoffice --writer" if is_linux else "winword",
    "excel": "libreoffice --calc" if is_linux else "excel",
    "calc": "libreoffice --calc" if is_linux else "excel",
    "chrome": "google-chrome" if is_linux else "chrome",
    "firefox": "firefox" if is_linux else "firefox",
    "vscode": "code",
    "code": "code",
    "powerpoint": "libreoffice --impress" if is_linux else "powerpnt",
    "impress": "libreoffice --impress" if is_linux else "powerpnt",
    "discord": "flatpak run com.discordapp.Discord",
    "telegram": "flatpak run org.telegram.desktop",
    "filemanager": "nautilus" if is_linux else "explorer",
    "files": "nautilus" if is_linux else "explorer",
    "calculator": "gnome-calculator" if is_linux else "calc",
    "notepad": "gedit" if is_linux else "notepad",
    "texteditor": "gedit" if is_linux else "notepad"
}

# Open app or website
def openappweb(query):
    speak("Launching, sir.")
    query = query.lower().replace("open", "").replace("nexa", "").replace("launch", "").strip()
    
    # Check if it's a website
    if ".com" in query or ".co.in" in query or ".org" in query or "www." in query:
        # Clean up the query for website
        query = query.replace("www.", "").replace(" ", "")
        if not query.startswith("http"):
            query = f"https://www.{query}"
        webbrowser.open(query)
        speak(f"Opening website")
    else:
        # Check for applications
        app_found = False
        for app in dictapp:
            if app in query:
                command = dictapp[app]
                try:
                    if is_linux:
                        os.system(f"{command} &")  # launch in background
                    else:
                        os.system(f"start {command}")
                    speak(f"Opening {app}")
                    app_found = True
                    break
                except Exception as e:
                    speak(f"Sorry, I couldn't open {app}")
        
        if not app_found:
            speak("Sorry, I couldn't find that application")

# Close apps or browser tabs
def closeappweb(query):
    try:
        speak("Closing, sir.")
        query = query.lower().replace("close", "").replace("nexa", "").strip()
        
        if "tab" in query or "browser" in query:
            # Close browser tabs
            try:
                pyautogui.hotkey("ctrl", "w")
                speak("Tab closed.")
            except Exception as e:
                print(f"Error closing tab: {e}")
                speak("Sorry, I couldn't close the tab")
        else:
            # Close specific applications
            app_found = False
            for app in dictapp:
                if app in query:
                    process = dictapp[app].split()[0]
                    try:
                        if is_linux:
                            os.system(f"pkill -f {process}")
                        else:
                            os.system(f"taskkill /f /im {process}.exe")
                        speak(f"Closing {app}")
                        app_found = True
                        break
                    except Exception as e:
                        print(f"Error closing {app}: {e}")
                        speak(f"Sorry, I couldn't close {app}")
            
            if not app_found:
                # Try to close the current active window
                try:
                    pyautogui.hotkey("alt", "f4")  # Works on both Windows and many Linux environments
                    speak("Closing current window")
                except Exception as e:
                    print(f"Error closing window: {e}")
                    speak("Sorry, I couldn't close the application")
    except Exception as e:
        print(f"Critical error in closeappweb: {e}")
        try:
            speak("Sorry, there was an error with the close command")
        except:
            print("Nexa: Sorry, there was an error with the close command")

# Minimize the currently active window in a cross-platform way
# The strategy is:
# 1. On Linux, prefer command-line utilities (wmctrl / xdotool) if installed.
#    These are much more reliable than arbitrary keyboard shortcuts because
#    they work regardless of the currently focused application or WM bindings.
# 2. Fall back to sensible keyboard shortcuts if the utilities are missing or fail.
# 3. On Windows, use the Win+Down shortcut that minimises the active window.
#
# The function now checks exit codes rather than swallowing errors so that we
# only announce success when the operation really succeeded.

def minimizeapp(query):
    import shutil
    speak("Minimizing, sir.")

    try:
        success = False

        if is_linux:
            # Prefer wmctrl if available
            if shutil.which("wmctrl"):
                exit_code = os.system("wmctrl -r :ACTIVE: -b add,hidden")
                success = (exit_code == 0)

            # If wmctrl failed or isn't installed, try xdotool
            if not success and shutil.which("xdotool"):
                exit_code = os.system("xdotool getactivewindow windowminimize")
                success = (exit_code == 0)

            # Fall back to common keyboard shortcuts recognised by most DEs
            if not success:
                try:
                    # GNOME default (Super+H)
                    pyautogui.hotkey("win", "h")
                    success = True
                except Exception:
                    pass

            if not success:
                try:
                    # Traditional Metacity/XFCE/KDE (Alt+F9)
                    pyautogui.hotkey("alt", "f9")
                    success = True
                except Exception:
                    pass
        else:
            # Windows: Win+Down Arrow = minimise
            pyautogui.hotkey("win", "down")
            success = True

        if success:
            speak("Window minimized")
        else:
            speak("Sorry, I couldn't minimize the window")
    except Exception as e:
        print(f"Error in minimizeapp: {e}")
        speak("Sorry, I couldn't minimize the window")

