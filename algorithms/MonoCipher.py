import string


class SubstitutionCipher:
    def __init__(self, key):
        alphabet = string.ascii_lowercase
        if len(key) != 26 or set(key.lower()) != set(alphabet):
            raise ValueError("Key must be a 26-letter permutation of the alphabet.")
        self.encrypt_dict = dict(zip(alphabet, key.lower()))
        self.decrypt_dict = dict(zip(key.lower(), alphabet))

    def encrypt(self, text):
        return "".join(self.encrypt_dict.get(c.lower(), c) for c in text)

    def decrypt(self, text):
        return "".join(self.decrypt_dict.get(c.lower(), c) for c in text)
