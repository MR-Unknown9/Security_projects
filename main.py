import customtkinter as ctk
from gui.GUI import TextProcessorApp

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    # Create main window
    root = ctk.CTk()

    # Create the app instance
    app = TextProcessorApp(root)

    # Run the application
    root.mainloop()
