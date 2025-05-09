import customtkinter as ctk
import pyperclip
import tkinter.filedialog as filedialog
import tkinter.messagebox as msgbox

# <====Algorithms====>
from algorithms.AutoKey import AutokeyCipher
from algorithms.ceaser import CaesarCipher
from algorithms.des import DESCipher
from algorithms.MonoCipher import SubstitutionCipher
from algorithms.playfair import PlayfairCipher
from algorithms.poly import VigenereCipher
from algorithms.railFence import RailFenceCipher

class TextProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("750x650")
        self.root.title("Text Processor")

        # GUI Setup
        self.create_widgets()

    def create_widgets(self):
        # Title
        title = ctk.CTkLabel(
            self.root, text="Text Processor", font=ctk.CTkFont(size=20, weight="bold")
        )
        title.pack(pady=10)

        # Input Section
        input_label = ctk.CTkLabel(self.root, text="Input Text:")
        input_label.pack(anchor="w", padx=20)
        self.input_text = ctk.CTkTextbox(self.root, height=80)
        self.input_text.pack(fill="x", padx=20, pady=(0, 10))

        # --- Top Control Row ---
        top_controls = ctk.CTkFrame(self.root)
        top_controls.pack(pady=5)

        upload_btn = ctk.CTkButton(
            top_controls, text="Upload File", command=self.upload_file
        )
        upload_btn.grid(row=0, column=0, padx=10)

        # Algorithm Dropdown
        self.algo_option = ctk.CTkOptionMenu(
            top_controls, values=["AutoKey", "Caesar", "Vigenère", "RailFence"]
        )
        self.algo_option.set("AutoKey")
        self.algo_option.grid(row=0, column=1, padx=10)

        # Encode/Decode Option
        self.action_option = ctk.CTkOptionMenu(
            top_controls, values=["Encode", "Decode"]
        )
        self.action_option.set("Encode")
        self.action_option.grid(row=0, column=2, padx=10)

        submit_btn = ctk.CTkButton(
            top_controls, text="Process", command=self.process_text
        )
        submit_btn.grid(row=0, column=3, padx=10)

        # Caesar Shift Value Entry
        self.caesar_shift_entry = ctk.CTkEntry(self.root, placeholder_text="Shift (Caesar)")
        self.caesar_shift_entry.pack(fill="x", padx=20, pady=(5, 10))

        # Output Section
        output_label = ctk.CTkLabel(self.root, text="Output:")
        output_label.pack(anchor="w", padx=20)
        self.output_text = ctk.CTkTextbox(self.root, height=80, state="disabled")
        self.output_text.pack(fill="x", padx=20, pady=(0, 10))

        # --- Second Control Row ---
        bottom_controls = ctk.CTkFrame(self.root)
        bottom_controls.pack(pady=10)

        copy_btn = ctk.CTkButton(
            bottom_controls, text="Copy Output", command=self.copy_to_clipboard
        )
        copy_btn.grid(row=0, column=0, padx=10)

        clear_btn = ctk.CTkButton(
            bottom_controls, text="Clear Fields", command=self.clear_fields
        )
        clear_btn.grid(row=0, column=1, padx=10)

        clear_history_btn = ctk.CTkButton(
            bottom_controls, text="Clear History", command=self.clear_history
        )
        clear_history_btn.grid(row=0, column=2, padx=10)

        theme_btn = ctk.CTkButton(
            bottom_controls, text="Toggle Theme", command=self.toggle_theme
        )
        theme_btn.grid(row=0, column=3, padx=10)

        # History Section
        history_label = ctk.CTkLabel(self.root, text="History:")
        history_label.pack(anchor="w", padx=20)
        self.history_text = ctk.CTkTextbox(self.root, height=150, state="disabled")
        self.history_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def process_text(self):
        text = self.input_text.get("1.0", "end-1c").strip()
        algo = self.algo_option.get()
        action = self.action_option.get()

        if not text:
            msgbox.showwarning("Input Required", "Please enter some text!")
            return

        try:
            if algo == "AutoKey":
                auto_key = AutokeyCipher(text)

                if action == "Encode":
                    result = auto_key.encrypt(text)
                    key_used = text
                else:
                    result = auto_key.decrypt(text)
                    key_used = text

            elif algo == "Caesar":
                try:
                    shift = int(self.caesar_shift_entry.get())
                    caesar_cipher = CaesarCipher(shift)

                    if action == "Encode":
                        result = caesar_cipher.encrypt(text)
                    else:
                        result = caesar_cipher.decrypt(text)
                    key_used = str(shift)
                except ValueError:
                    msgbox.showwarning("Invalid Shift", "Please enter a valid integer for Caesar shift.")
                    return

            elif algo == "Vigenère":
                key = self.input_text.get("1.0", "end-1c").strip()
                vigenere_cipher = VigenereCipher(key)

                if action == "Encode":
                    result = vigenere_cipher.encrypt(text)
                else:
                    result = vigenere_cipher.decrypt(text)
                key_used = key

            elif algo == "RailFence":
                rails = int(self.input_text.get("1.0", "end-1c").strip())
                rail_fence_cipher = RailFenceCipher()

                if action == "Encode":
                    result = rail_fence_cipher.encode(text, rails)
                else:
                    result = rail_fence_cipher.decode(text, rails)
                key_used = str(rails)

            else:
                result = "Algorithm not implemented."
                key_used = "N/A"

            self.output_text.configure(state="normal")
            self.output_text.delete("1.0", "end")
            self.output_text.insert("end", result)
            self.output_text.configure(state="disabled")

            # Add to history
            history_entry = f"[{algo} - {action}]\nKey: {key_used}\nInput: {text}\nOutput: {result}\n{'-'*40}\n"
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
        self.caesar_shift_entry.delete(0, "end")
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
