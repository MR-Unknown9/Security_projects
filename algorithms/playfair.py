class PlayfairCipher:
    def __init__(self, key):
        key = key.upper().replace("J", "I")
        seen = []
        for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if c.isalpha() and c not in seen:
                seen.append(c)
        self.matrix = [seen[i : i + 5] for i in range(0, 25, 5)]

    def __find(self, c):
        if c == "J":
            c = "I"
        for r, row in enumerate(self.matrix):
            if c in row:
                return r, row.index(c)

    def __pair_text(self, text):
        text = text.upper().replace("J", "I").replace(" ", "")
        i, pairs = 0, []
        while i < len(text):
            a = text[i]
            b = text[i + 1] if i + 1 < len(text) else "X"
            if a == b:
                b = "X"
                i += 1
            else:
                i += 2
            pairs.append((a, b))
        return pairs

    def __translate(self, pairs, shift):
        out = ""
        for a, b in pairs:
            r1, c1 = self.__find(a)
            r2, c2 = self.__find(b)
            if r1 == r2:
                out += self.matrix[r1][(c1 + shift) % 5]
                out += self.matrix[r2][(c2 + shift) % 5]
            elif c1 == c2:
                out += self.matrix[(r1 + shift) % 5][c1]
                out += self.matrix[(r2 + shift) % 5][c2]
            else:
                out += self.matrix[r1][c2]
                out += self.matrix[r2][c1]
        return out

    def encrypt(self, text):
        return self.__translate(self.__pair_text(text), 1)

    def decrypt(self, text):
        return self.__translate(self.__pair_text(text), -1)
