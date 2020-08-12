class Yenigma:
    def __init__(self):
        self.set_base(3)
        pass

    def set_base(self, number_of_rings, ring_set="abcdefghijklmnopqrstuvwxyz"):
        self.ring_chars = ring_set
        self.ring_count = number_of_rings
        self.rotors = [list(self.ring_chars)] * self.ring_count
        self.rotations = [0]*self.ring_count
        self.reflector = dict(zip(self.ring_chars, self.ring_chars))
        self.full_set = [self.rotors, self.reflector]

        return self.full_set

    def rotor_f(self, char, ring):
        if (loc := self.ring_chars.find(char)) == -1:
            return ""
        else:
            return self.rotors[ring][loc]

    def rotor_b(self, char, ring):
        if char in self.ring_chars:
            return self.rotors[ring][self.ring_chars.index(char)]
        else:
            return ""


if __name__ == '__main__':
    yenigma = Yenigma()

    print(yenigma.rotor_b("a", 1))
