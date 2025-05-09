# 🧠 Text Encoder / Decoder App
A simple and interactive GUI application that lets you encode or decode text using various classical cryptographic algorithms. Built with Python and CustomTkinter — ideal for students, enthusiasts, and cybersecurity beginners.

## ✨ Features
- Encode and decode text using:
  - AutoKey Cipher
  - Caesar Cipher
  - Vigenère Cipher
  - RailFence Cipher
  - Monoalphabetic Substitution Cipher
  - Playfair Cipher
  - DES (Simplified)
- Upload a `.txt` file for input
- Copy output to clipboard
- Clear input/output fields
- View and clear history
- Toggle between Light and Dark mode

## 📁 Project Structure
```
Security\_project/
├── algorithms/
│   ├── AutoKey.py         # AutoKey Cipher
│   ├── ceaser.py          # Caesar Cipher
│   ├── des.py             # Simplified DES Cipher
│   ├── MonoCipher.py      # Monoalphabetic Substitution Cipher
│   ├── playfair.py        # Playfair Cipher
│   ├── poly.py            # Vigenère Cipher
│   └── railFence.py       # RailFence Cipher
├── gui.py                # GUI layout and behavior
├── main.py               # Entry point to launch the app
└── README.md             # This file
```

## 🛠 Requirements
- Python 3.10+
- Install dependencies with:
```bash
pip install -r requirements.txt
```

## 🚀 How to Run
```bash
python main.py
```

## 📦 Supported Algorithms
| Algorithm        | Encode | Decode |
|------------------|--------|--------|
| AutoKey          | ✅     | ✅     |
| Caesar           | ✅     | ✅     |
| Vigenère         | ✅     | ✅     |
| RailFence        | ✅     | ✅     |
| Monoalphabetic   | ✅     | ✅     |
| Playfair         | ✅     | ✅     |
| DES (Simplified) | ✅     | ✅     |

## 🎓 Use Cases
* Cryptography exercises
* Cybersecurity and ethical hacking workshops
* Class projects involving secure communication concepts

## 📌 Notes
* This app is meant for educational use only.
* Easily extendable with more algorithms like RSA, Hashing, etc.

Made with ❤️ for learning, experimenting, and cryptographic curiosity.
