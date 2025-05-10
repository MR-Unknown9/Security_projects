# cipher.py

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        return self._cipher(text, encode=True)

    def decrypt(self, text):
        return self._cipher(text, encode=False)

    def _cipher(self, text, encode=True):
        result = ''
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                offset = self.shift if encode else -self.shift
                result += chr((ord(char) - base + offset) % 26 + base)
            else:
                result += char
        return result
