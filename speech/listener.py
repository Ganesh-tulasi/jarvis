import speech_recognition as sr
import config

def listen():
    """
    Listens to the microphone and returns the recognized text.
    Uses Google Speech Recognition by default.
    """
    recognizer = sr.Recognizer()
    
    # Optional: adjust energy threshold dynamically
    recognizer.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("[Listener] Listening...")
        try:
            # phrase_time_limit prevents listening forever if background noise is continuous
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return ""

    try:
        text = recognizer.recognize_google(audio)
        print(f"\n[User] {text}")
        return text.lower()
    except sr.UnknownValueError:
        # Unrecognizable speech
        return ""
    except sr.RequestError as e:
        print(f"[Listener] Google Speech Recognition service error: {e}")
        return ""
    except Exception as e:
        print(f"[Listener] Error: {e}")
        return ""
