from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

class DESCipher:
    def __init__(self, key):
        self.key = key  # Must be 8 bytes for DES
        self.block_size = DES.block_size

    def encrypt(self, data):
        cipher = DES.new(self.key, DES.MODE_ECB)
        encrypted_data = cipher.encrypt(pad(data, self.block_size))
        return encrypted_data

    def decrypt(self, encrypted_data):
        decipher = DES.new(self.key, DES.MODE_ECB)
        decrypted_data = unpad(decipher.decrypt(encrypted_data), self.block_size)
        return decrypted_data
