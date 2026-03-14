import os
from speech.speaker import speak

def take_screenshot():
    speak("Taking a screenshot.")
    try:
        import pyautogui
        import config
        desktop = config.DESKTOP_DIR
        # simple screenshot using pyautogui
        img = pyautogui.screenshot()
        img.save(os.path.join(desktop, "jarvis_screenshot.png"))
        return "Screenshot saved to your desktop."
    except ImportError:
        print("pyautogui not installed")
        return "I need the pyautogui package to take a screenshot."
    except Exception as e:
        print(f"Failed to screenshot: {e}")
        return "Sorry, I couldn't take a screenshot."

def adjust_volume(query):
    speak("Adjusting system volume.")
    try:
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        current_vol = volume.GetMasterVolumeLevelScalar()
        
        if "up" in query or "increase" in query:
            new_vol = min(1.0, current_vol + 0.1)
            volume.SetMasterVolumeLevelScalar(new_vol, None)
            volume.SetMute(0, None)
            return "Volume increased."
        elif "down" in query or "decrease" in query:
            new_vol = max(0.0, current_vol - 0.1)
            volume.SetMasterVolumeLevelScalar(new_vol, None)
            volume.SetMute(0, None)
            return "Volume decreased."
        elif "mute" in query:
            volume.SetMute(1, None)
            return "Volume muted."
        elif "unmute" in query:
            volume.SetMute(0, None)
            return "Volume unmuted."
        else:
            # Try to extract a number from the query to set exact volume
            import re
            match = re.search(r'\b(\d{1,3})\b', query)
            if match:
                level = int(match.group(1))
                # clamp between 0 and 100
                level = max(0, min(100, level))
                
                volume.SetMasterVolumeLevelScalar(level / 100.0, None)
                volume.SetMute(0, None)
                return f"Volume set to {level} percent."
            
        return "Volume adjusted."
    except ImportError:
        return "I need the pycaw package to adjust volume safely."
    except Exception as e:
        print(f"Volume error: {e}")
        return "Could not adjust the volume at this time."
