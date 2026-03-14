import time
from speech.listener import listen
from speech.speaker import speak
from brain.agent import process_query
import config
import ui.dashboard as ui

def main():
    ui.launch()
    ui.update_status("System Online")
    
    msg = "Starting JARVIS. System initialization complete."
    ui.update_response(msg)
    speak(msg)
    
    msg = f"Listening for wake word: {config.WAKE_WORD}"
    ui.update_response(msg)
    speak(msg)
    
    while True:
        try:
            ui.update_status("Listening for wake word...")
            text = listen()
            if text:
                ui.update_user_cmd(text)
            
            if not text:
                time.sleep(0.1)
                continue
                
            print(f"Heard continuously: {text}")
            
            if config.WAKE_WORD in text:
                ui.update_status("Awake. Listening to command...")
                speak("Yes sir?")
                
                command = listen()
                if command:
                    ui.update_user_cmd(command)
                    ui.update_status("Processing...")
                    response = process_query(command)
                    ui.update_response(response)
                    speak(response)
                else:
                    msg = "I didn't catch that."
                    ui.update_response(msg)
                    speak(msg)
            elif "exit jarvis" in text or "shutdown jarvis" in text:
                msg = "Shutting down. Goodbye."
                ui.update_status("Offline")
                ui.update_response(msg)
                speak(msg)
                break
        except KeyboardInterrupt:
            speak("Keyboard interrupt detected. Shutting down.")
            break
        except Exception as e:
            print(f"Unhandled error in main loop: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()
