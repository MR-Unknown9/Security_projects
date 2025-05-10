class RailFenceCipher:
    def __init__(self, rails):
        self.rails = rails

    def encrypt(self, text):
        if self.rails < 2:
            return text

        fence = ["" for _ in range(self.rails)]
        rail = 0
        step = 1

        for char in text:
            fence[rail] += char
            rail += step
            if rail == 0 or rail == self.rails - 1:
                step *= -1

        return "".join(fence)

    def decrypt(self, text):
        if self.rails < 2:
            return text

        pattern = []
        rail = 0
        step = 1
        for _ in text:
            pattern.append(rail)
            rail += step
            if rail == 0 or rail == self.rails - 1:
                step *= -1

        rail_lengths = [pattern.count(r) for r in range(self.rails)]

        rails_data = []
        i = 0
        for length in rail_lengths:
            rails_data.append(list(text[i : i + length]))
            i += length

        result = ""
        rail_positions = [0] * self.rails
        for r in pattern:
            result += rails_data[r][rail_positions[r]]
            rail_positions[r] += 1

        return result
