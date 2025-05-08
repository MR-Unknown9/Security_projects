# 🧠 Text Encoder / Decoder App
A simple and interactive GUI application that lets you encode or decode text using various algorithms like Base64, ROT13, and Reverse. Built with Python and CustomTkinter — perfect for students and cybersecurity beginners.

## ✨ Features
- Encode and decode text using:
  - Base64
  - ROT13
  - Reverse
- Upload a `.txt` file for input
- Copy output to clipboard
- Clear input/output fields
- View and clear history
- Toggle between Light and Dark mode

## 📁 Project Structure
```
Security\_project/
├── alg.py         # Logic for text encoding/decoding
├── gui.py         # GUI layout and behavior
├── main.py        # Entry point to launch the app
└── README.md      # This file
````

## 🛠 Requirements
- Python 3.10+
- Install dependencies with:
```bash
pip install -r requirements.txt
````
Or manually:
```bash
pip install customtkinter pyperclip
```

## 🚀 How to Run
```bash
python main.py
```

## 📦 Supported Algorithms
| Algorithm | Encode | Decode |
| --------- | ------ | ------ |
| Base64    | ✅      | ✅      |
| ROT13     | ✅      | ✅      |
| Reverse   | ✅      | ✅      |

## 🎓 Use Cases
* Cryptography exercises
* Cybersecurity workshops
* Quick encoding/decoding tool for class projects

## 📌 Notes
* This app is meant for educational use.
* More algorithms and features (like hashing, encryption) can be added easily.

Made with ❤️ for learning and exploration.
