import pyttsx3
import config

# Initialize TTS Engine
engine = pyttsx3.init()

# Setup properties from config
engine.setProperty('rate', config.TTS_RATE)
engine.setProperty('volume', config.TTS_VOLUME)

# Set Voice Gender
voices = engine.getProperty('voices')
if config.TTS_VOICE_GENDER.lower() == 'female':
    # Usually index 1 is female on Windows Zira
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
else:
    # Usually index 0 is male on Windows David
    if len(voices) > 0:
        engine.setProperty('voice', voices[0].id)

def speak(text):
    """
    Speaks the given text out loud using pyttsx3.
    """
    if not text:
        return
    print(f"[JARVIS] {text}")
    engine.say(text)
    engine.runAndWait()
