class AutokeyCipher:
    def __init__(self, key):
        self.initial_key = key.upper()

    def generate_key(self, message):
        key = list(self.initial_key)
        message = message.upper().replace(" ", "")
        while len(key) < len(message):
            key.append(message[len(key)])
        return "".join(key)

    def encrypt(self, plaintext):
        plaintext = plaintext.upper().replace(" ", "")
        key = self.generate_key(plaintext)
        ciphertext = ""
        for p, k in zip(plaintext, key):
            c = chr(((ord(p) - 65 + ord(k) - 65) % 26) + 65)
            ciphertext += c
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper().replace(" ", "")
        key = self.initial_key
        plaintext = ""
        for i in range(len(ciphertext)):
            k = key[i] if i < len(key) else plaintext[i - len(key)]
            p = chr(((ord(ciphertext[i]) - ord(k) + 26) % 26) + 65)
            plaintext += p
            if i >= len(key):
                key += p  # dynamically extend the key with the decrypted plaintext
        return plaintext
