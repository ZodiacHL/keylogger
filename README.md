# 🔐 Encrypted Keylogger (Educational Project)

This project is a simple **keylogger with encrypted logging** functionality built in Python using `pynput` and `cryptography`. It captures keyboard input and stores it in an encrypted file to help students and beginners understand input handling, basic encryption, and secure logging.

> ⚠️ This tool is for **educational purposes only**. Do not use this software without clear permission on any system you do not own or manage.

---

## 🧰 Features

- Logs every keystroke (character + timestamp)
- Encrypts all entries using `Fernet` symmetric encryption
- Logs are stored in a secure `.enc` file

---

## 🛠️ Requirements

- Python 3.x
- `pynput`  
- `cryptography`  

Install dependencies:
```bash
pip install pynput cryptography
```
## 🚀 How to Run
1. Generate Encryption Key
Run once to create key.key:

```bash
python generate_key.py
```
2. Start Logging
Run the keylogger:

```bash
python keylogger.py
```
✅ Press ESC to stop logging.

## 🔓 Decrypting Logs
To view the contents of the encrypted logs:

```python
from cryptography.fernet import Fernet

with open("key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

with open("keylog.enc", "rb") as log_file:
    for line in log_file:
        decrypted = fernet.decrypt(line.strip())
        print(decrypted.decode())
```
## 📁 Files
generate_key.py – Creates and saves the encryption key

keylogger.py – Main script that logs and encrypts keystrokes

key.key – Generated key file (keep this secret!)

keylog.enc – Encrypted keystroke log file

## ✅ Educational Value
This project helps you practice:

Keyboard event capture

Secure data handling

Working with external libraries

Understanding file I/O and encryption

## 🔐 Disclaimer
This tool is strictly for learning purposes. Using keyloggers in any malicious or unauthorized way is unethical and illegal in many jurisdictions.
