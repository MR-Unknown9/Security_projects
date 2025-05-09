class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def _process_text(self, text, mode="encrypt"):
        processed_text = ""
        key_index = 0
        key_length = len(self.key)

        for char in text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                shift = ord(self.key[key_index % key_length]) - 65
                if mode == "encrypt":
                    processed_char = chr((ord(char) - offset + shift) % 26 + offset)
                elif mode == "decrypt":
                    processed_char = chr(
                        (ord(char) - offset - shift + 26) % 26 + offset
                    )
                processed_text += processed_char
                key_index += 1
            else:
                processed_text += char
        return processed_text

    def encrypt(self, text):
        return self._process_text(text, mode="encrypt")

    def decrypt(self, text):
        return self._process_text(text, mode="decrypt")
