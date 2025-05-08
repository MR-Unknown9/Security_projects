# main.py
import customtkinter as ctk
from gui.GUI import EncoderDecoderApp

if __name__ == "__main__":
    root = ctk.CTk()
    app = EncoderDecoderApp(root)
    root.mainloop()
