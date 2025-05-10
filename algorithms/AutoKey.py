class AutoKeyCipher:
    def __init__(self, key):
        self.key = key

    def generate_key(self, message):
        key = list(self.key.upper())
        if len(key) < len(message):
            key += list(message[: len(message) - len(key)])
        return "".join(key)

    def encrypt(self, plaintext):
        plaintext = plaintext.upper().replace(" ", "")
        key = self.generate_key(plaintext)
        cipher_text = ""
        for p, k in zip(plaintext, key):
            c = chr(((ord(p) + ord(k)) % 26) + 65)
            cipher_text += c
        return cipher_text

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper().replace(" ", "")
        key = self.key.upper()
        plaintext = ""
        for i in range(len(ciphertext)):
            if i < len(key):
                k = key[i]
            else:
                k = plaintext[i - len(key)]
            p = chr(((ord(ciphertext[i]) - ord(k) + 26) % 26) + 65)
            plaintext += p
        return plaintext
