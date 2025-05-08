# gui.py
import customtkinter as ctk
import pyperclip
import tkinter.messagebox as msgbox
import tkinter.filedialog as filedialog
from algorithom.test import base64_encode, base64_decode, reverse_text, rot13


class EncoderDecoderApp:
    def __init__(self, root):
        self.app = root
        self.app.geometry("750x650")
        self.app.title("Text Encoder/Decoder")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.build_ui()

    def build_ui(self):
        self.title = ctk.CTkLabel(
            self.app,
            text="Text Encoder / Decoder",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.title.pack(pady=10)

        self.input_label = ctk.CTkLabel(self.app, text="Input Text:")
        self.input_label.pack(anchor="w", padx=20)
        self.input_text = ctk.CTkTextbox(self.app, height=80)
        self.input_text.pack(fill="x", padx=20, pady=(0, 10))

        self.top_controls = ctk.CTkFrame(self.app)
        self.top_controls.pack(pady=5)

        self.upload_btn = ctk.CTkButton(
            self.top_controls, text="Upload File", command=self.upload_file
        )
        self.upload_btn.grid(row=0, column=0, padx=10)

        self.algo_option = ctk.CTkOptionMenu(
            self.top_controls, values=["Base64", "Reverse", "ROT13"]
        )
        self.algo_option.set("Base64")
        self.algo_option.grid(row=0, column=1, padx=10)

        self.mode_option = ctk.CTkOptionMenu(
            self.top_controls, values=["Encode", "Decode"]
        )
        self.mode_option.set("Encode")
        self.mode_option.grid(row=0, column=2, padx=10)

        self.submit_btn = ctk.CTkButton(
            self.top_controls, text="Process", command=self.process_text
        )
        self.submit_btn.grid(row=0, column=3, padx=10)

        self.output_label = ctk.CTkLabel(self.app, text="Output:")
        self.output_label.pack(anchor="w", padx=20)
        self.output_text = ctk.CTkTextbox(self.app, height=80, state="disabled")
        self.output_text.pack(fill="x", padx=20, pady=(0, 10))

        self.bottom_controls = ctk.CTkFrame(self.app)
        self.bottom_controls.pack(pady=10)

        self.copy_btn = ctk.CTkButton(
            self.bottom_controls, text="Copy Output", command=self.copy_to_clipboard
        )
        self.copy_btn.grid(row=0, column=0, padx=10)

        self.clear_btn = ctk.CTkButton(
            self.bottom_controls, text="Clear Fields", command=self.clear_fields
        )
        self.clear_btn.grid(row=0, column=1, padx=10)

        self.clear_history_btn = ctk.CTkButton(
            self.bottom_controls, text="Clear History", command=self.clear_history
        )
        self.clear_history_btn.grid(row=0, column=2, padx=10)

        self.theme_btn = ctk.CTkButton(
            self.bottom_controls, text="Toggle Theme", command=self.toggle_theme
        )
        self.theme_btn.grid(row=0, column=3, padx=10)

        self.history_label = ctk.CTkLabel(self.app, text="History:")
        self.history_label.pack(anchor="w", padx=20)
        self.history_text = ctk.CTkTextbox(self.app, height=150, state="disabled")
        self.history_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def process_text(self):
        text = self.input_text.get("1.0", "end-1c").strip()
        algo = self.algo_option.get()
        mode = self.mode_option.get()

        if not text:
            msgbox.showwarning("Input Required", "Please enter some text!")
            return

        try:
            if algo == "Base64":
                result = (
                    base64_encode(text) if mode == "Encode" else base64_decode(text)
                )
            elif algo == "Reverse":
                result = reverse_text(text)
            elif algo == "ROT13":
                result = rot13(text)
            else:
                result = "Algorithm not implemented."

            self.output_text.configure(state="normal")
            self.output_text.delete("1.0", "end")
            self.output_text.insert("end", result)
            self.output_text.configure(state="disabled")

            history_entry = (
                f"[{mode} | {algo}]\nInput: {text}\nOutput: {result}\n{'-'*40}\n"
            )
            self.history_text.configure(state="normal")
            self.history_text.insert("end", history_entry)
            self.history_text.configure(state="disabled")

        except Exception as e:
            msgbox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        text = self.output_text.get("1.0", "end-1c")
        if text:
            pyperclip.copy(text)
            msgbox.showinfo("Copied", "Output copied to clipboard!")

    def clear_fields(self):
        self.input_text.delete("1.0", "end")
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.configure(state="disabled")

    def clear_history(self):
        self.history_text.configure(state="normal")
        self.history_text.delete("1.0", "end")
        self.history_text.configure(state="disabled")

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.input_text.delete("1.0", "end")
                    self.input_text.insert("end", content)
            except Exception as e:
                msgbox.showerror("Error", f"Failed to read file:\n{str(e)}")

    def toggle_theme(self):
        current = ctk.get_appearance_mode()
        ctk.set_appearance_mode("Dark" if current == "Light" else "Light")
