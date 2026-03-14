import webbrowser
import pywhatkit
from speech.speaker import speak

def open_browser():
    speak("Opening the browser.")
    webbrowser.open("https://www.google.com")
    return "Opened the browser."

def search_google(query):
    speak(f"Searching Google for {query}.")
    try:
        pywhatkit.search(query)
        return f"I have searched Google for {query}."
    except Exception as e:
        print(f"Error searching Google: {e}")
        return "Sorry, I couldn't reach Google right now."

def search_youtube(query):
    speak(f"Searching YouTube for {query}.")
    try:
        pywhatkit.playonyt(query)
        return f"Playing {query} on YouTube."
    except Exception as e:
        print(f"Error playing on YouTube: {e}")
        return "Sorry, I couldn't play that on YouTube."
