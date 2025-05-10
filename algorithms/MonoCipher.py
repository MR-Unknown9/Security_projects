import string


class MonoalphabeticCipher:
    def __init__(self, key):
        original_alphabet = string.ascii_lowercase
        if not self._is_valid_key(key, original_alphabet):
            raise ValueError("Key must be a 26-letter permutation of the alphabet.")
        self.encrypt_dict = dict(zip(original_alphabet, key))
        self.decrypt_dict = dict(zip(key, original_alphabet))

    def _is_valid_key(self, key, original_alphabet):
        return len(key) == 26 and set(key) == set(original_alphabet)

    def encrypt(self, text):
        text = text.lower()
        return "".join(self.encrypt_dict.get(c, c) for c in text)

    def decrypt(self, text):
        text = text.lower()
        return "".join(self.decrypt_dict.get(c, c) for c in text)
