# alg.py
import base64


def base64_encode(text):
    return base64.b64encode(text.encode()).decode()


def base64_decode(text):
    return base64.b64decode(text.encode()).decode()


def reverse_text(text):
    return text[::-1]


def rot13(text):
    return text.translate(
        str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm",
        )
    )
