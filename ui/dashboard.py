import tkinter as tk
import threading
import time

class JarvisUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS Assistant")
        self.root.geometry("400x250")
        self.root.configure(bg="#0f0f0f")
        self.root.attributes("-topmost", True)

        self.label_title = tk.Label(
            self.root, text="J.A.R.V.I.S.",
            font=("Helvetica", 20, "bold"), fg="#00ccff", bg="#0f0f0f"
        )
        self.label_title.pack(pady=10)

        self.label_status = tk.Label(
            self.root, text="Initializing...",
            font=("Helvetica", 12), fg="white", bg="#0f0f0f"
        )
        self.label_status.pack(pady=5)

        self.label_cmd = tk.Label(
            self.root, text="",
            font=("Helvetica", 10, "italic"), fg="#aaffaa", bg="#0f0f0f"
        )
        self.label_cmd.pack(pady=5)

        self.label_res = tk.Label(
            self.root, text="",
            font=("Helvetica", 10), fg="white", bg="#0f0f0f", wraplength=350
        )
        self.label_res.pack(pady=10)

    def set_status(self, text):
        self.label_status.config(text=text)

    def set_cmd(self, text):
        self.label_cmd.config(text=f"User: {text}")

    def set_res(self, text):
        self.label_res.config(text=f"JARVIS: {text}")

_ui = None

def _run_ui():
    global _ui
    root = tk.Tk()
    _ui = JarvisUI(root)
    root.mainloop()

def launch():
    """Starts the tkinter mainloop in a separate thread."""
    t = threading.Thread(target=_run_ui, daemon=True)
    t.start()
    # give it a moment to boot
    time.sleep(1)

def update_status(text):
    if _ui and _ui.root:
        try:
            _ui.root.after(0, _ui.set_status, text)
        except Exception:
            pass

def update_user_cmd(text):
    if _ui and _ui.root:
        try:
            _ui.root.after(0, _ui.set_cmd, text)
        except Exception:
            pass

def update_response(text):
    if _ui and _ui.root:
        try:
            _ui.root.after(0, _ui.set_res, text)
        except Exception:
            pass
