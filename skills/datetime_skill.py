from datetime import datetime
from speech.speaker import speak

def get_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The time is {current_time}.")
    return f"It is {current_time}."

def get_date():
    now = datetime.now()
    current_date = now.strftime("%A, %B %d, %Y")
    speak(f"Today is {current_date}.")
    return f"Today is {current_date}."
