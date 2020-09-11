class Yenigma:
    import warnings
    from typing import Union
    import randomish

    def __init__(self):
        self.set_base(3)
        pass

    def set_base(self, number_of_rings, ring_set="abcdefghijklmnopqrstuvwxyz"):
        self.ring_chars = ring_set
        self.ring_count = number_of_rings
        self.rotors = [list(self.ring_chars) for _ in range(self.ring_count)]
        self.rotations = [0] * self.ring_count
        self.reflector = dict(zip(self.ring_chars, self.ring_chars))
        self.plugboard = dict()
        self.full_set = [self.rotors, self.reflector]

        return self.full_set

    def create_rotors(self, keys: Union[tuple, list], ):
        if (len(keys)) != 2 or (len(keys[0]) != self.ring_count):
            self.warnings.warn("The format isn't correct. Unable to create rotors.")
            return None

        for ring in range(len(keys[0])):
            self.create_rotor(ring, keys[0][ring])
        self.create_reflector(keys[1])

    def create_rotor(self, ring, key):
        self.randomish.set_seed(key)

        temp_rotor = []
        temp_chars = list(self.ring_chars)

        for item in range(len(temp_chars)):
            temp_rotor.append(temp_chars.pop(self.randomish.random_int(len(temp_chars))))

        self.rotors[ring] = temp_rotor
        return

    def create_reflector(self, key):
        self.randomish.set_seed(key)

        temp_reflector = dict()
        temp_char = list(self.ring_chars)
        while len(temp_char):
            rand = (self.randomish.random_int(len(temp_char)), self.randomish.random_int(len(temp_char)))
            a, b = min(rand), max(rand)
            temp_reflector[temp_char[a]] = temp_char[b]
            temp_reflector[temp_char[b]] = temp_char[a]
            del temp_char[a]
            if a != b:
                del temp_char[b-1]
        self.reflector = temp_reflector

        return

    def create_pb(self, link: Union[list, tuple]):
        temp_pb = dict()
        for two in link:
            if (two[0] in self.ring_chars) and (two[1] in self.ring_chars):
                temp_pb[two[1]] = two[0]
                temp_pb[two[0]] = two[1]
        self.plugboard = temp_pb

        return

    def rotor_base(self, keys: Union[list, tuple]):
        for rotor in range(len(keys)):
            self.rotate(rotor, quantity=keys[rotor])

    def rotor_start(self, keys: Union[list, tuple]):
        for rotor in range(len(keys)):
            self.rotate(rotor, quantity=keys[rotor])
            self.add_rotation(rotor, keys[rotor])

    def rotor_f(self, char, ring):
        if char in self.ring_chars:
            return self.rotors[ring][self.ring_chars.index(char)]
        else:
            return

    def rotor_b(self, char, ring):
        if char in self.ring_chars:
            return self.ring_chars[self.rotors[ring].index(char)]
        else:
            return

    def reflect(self, char):
        if char in self.ring_chars:
            return self.reflector[char]
        else:
            return

    def reroute(self, char):
        try:
            return self.plugboard[char], True
        except KeyError:
            return char, False

    def rotate(self, ring, quantity=1):
        for i in range(quantity):
            self.rotors[ring].append(self.rotors[ring].pop(0))

        return self.rotors[ring]

    def add_rotation(self, ring, quantity=1):
        self.rotate(ring, quantity=quantity)
        self.rotations[ring] += quantity
        self.check_rotation()

        return self.rotations

    def check_rotation(self):
        for ring in range(len(self.rotors)):
            while self.rotations[ring] >= len(self.ring_chars):
                self.rotations[ring] -= len(self.ring_chars)
                if ring != (len(self.rotors) - 1):
                    self.rotations[ring + 1] += 1

    def crypt(self, text, enc=True):
        crypted = ""
        for char in text:
            curr = char
            turn = 1
            curr, fThrough = self.reroute(curr)
            for rotor in range(len(self.rotors)):
                curr = self.rotor_f(curr, rotor)
            curr = self.reflect(curr)
            for rotor in range((len(self.rotors) - 1), -1, -1):
                curr = self.rotor_b(curr, rotor)
            curr, bThrough = self.reroute(curr)
            if (enc and fThrough) or ((not enc) and bThrough):
                turn = 2
            self.add_rotation(0, quantity=turn)

            crypted += curr

        return crypted


if __name__ == '__main__':
    yenigma = Yenigma()
    while True:
        try:
            print(eval(input()))
        except Exception as error:
            print(error)
