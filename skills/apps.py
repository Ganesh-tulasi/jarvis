import os
import subprocess
from speech.speaker import speak

# Map of common app names to executable names or paths (Windows)
APP_MAP = {
    "notepad": "notepad.exe",
    "cmd": "cmd.exe",
    "command prompt": "cmd.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "explorer": "explorer.exe",
    "files": "explorer.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "edge": "msedge.exe",
    "chrome": "chrome.exe",
    "browser": "chrome.exe",
    "vscode": "code",
    "code": "code",
    "settings": "start ms-settings:",
    "downloads": "explorer shell:downloads",
    "documents": "explorer shell:Personal",
    "pictures": "explorer shell:My Pictures",
    "desktop": "explorer shell:Desktop"
}

def launch_app(app_name):
    # Try to find exact match in our manual dictionary first
    for key, exe in APP_MAP.items():
        if key in app_name.lower():
            speak(f"Opening {key}.")
            try:
                # Need to use shell=True for 'start ms-settings:' or 'code'
                subprocess.Popen(exe, shell=True)
                return f"Successfully launched {key}."
            except Exception as e:
                print(e)
                return f"Failed to launch {key}."
                
    speak(f"Let me try to find {app_name}.")
    try:
        # Generic fallback using Windows start command
        os.system(f"start {app_name}")
        return f"Attempted to start {app_name}."
    except Exception as e:
        print(e)
        return "Sorry, I couldn't find that application."

def close_app(app_name):
    speak(f"Closing {app_name}.")
    exe_name = f"{app_name}.exe"
    for key, exe in APP_MAP.items():
        if key in app_name.lower() and not exe.startswith("start "):
            exe_name = exe
            break
            
    os.system(f"taskkill /f /im {exe_name} /t")
    return f"Closed {app_name}."
