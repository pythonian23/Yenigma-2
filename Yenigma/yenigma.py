class Yenigma:
    def __init__(self):
        self.set_base(3)
        pass

    def set_base(self, number_of_rings, ring_set="abcdefghijklmnopqrstuvwxyz"):
        self.ring_chars = ring_set
        self.ring_count = number_of_rings
        self.ring_set = list(self.ring_chars) * self.ring_count
        self.reflector = dict(zip(self.ring_chars, self.ring_chars))

        return self.ring_set


if __name__ == '__main__':
    yenigma = Yenigma()
    print(yenigma.reflector)
