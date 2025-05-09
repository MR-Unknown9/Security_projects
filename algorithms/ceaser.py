class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26

    def encode(self, text):
        return self._transform(text, self.shift)

    def decode(self, text):
        return self._transform(text, -self.shift)

    def _transform(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        return result
