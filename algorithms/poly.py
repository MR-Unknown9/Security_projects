class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def encrypt(self, plain_text):
        encrypted_text = ""
        key_length = len(self.key)
        key_index = 0

        for char in plain_text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                shift = ord(self.key[key_index % key_length]) - 65
                encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
                encrypted_text += encrypted_char
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, cipher_text):
        decrypted_text = ""
        key_length = len(self.key)
        key_index = 0

        for char in cipher_text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                shift = ord(self.key[key_index % key_length]) - 65
                decrypted_char = chr((ord(char) - offset - shift + 26) % 26 + offset)
                decrypted_text += decrypted_char
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text
