import os
from dotenv import load_dotenv

load_dotenv()

# Speech Recognition Settings
WAKE_WORD = "jarvis"
OFFLINE_MODE = False  # Set to True to use Vosk offline only

# Text to Speech Settings
TTS_RATE = 175
TTS_VOLUME = 1.0
TTS_VOICE_GENDER = "female"  # or "male"

# API Keys (optional)
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Output directories
DOWNLOADS_DIR = os.path.expanduser("~/Downloads")
DESKTOP_DIR = os.path.expanduser("~/Desktop")
