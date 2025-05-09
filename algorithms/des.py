from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


class DESCipher:
    def __init__(self, key: bytes):
        if len(key) != 8:
            raise ValueError("Key must be exactly 8 bytes for DES.")
        self.key = key
        self.block_size = DES.block_size

    def encrypt(self, data: bytes) -> bytes:
        cipher = DES.new(self.key, DES.MODE_ECB)
        return cipher.encrypt(pad(data, self.block_size))

    def decrypt(self, encrypted_data: bytes) -> bytes:
        cipher = DES.new(self.key, DES.MODE_ECB)
        return unpad(cipher.decrypt(encrypted_data), self.block_size)
