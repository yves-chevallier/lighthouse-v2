class LFSR:
    def __init__(self, poly, start=1):
        self.state = self.start = start
        self.poly = poly

    def reset(self):
        self.state = start

    def enter_loop(self):
        for i in range(2**17):
            next(self)
        return self

    def parity(self, bb):
        b = bb
        b ^= b >> 16
        b ^= b >> 8
        b ^= b >> 4
        b ^= b >> 2
        b ^= b >> 1
        b &= 1
        return b

    def __next__(self):
        b = self.state & self.poly
        b = self.parity(b)
        self.state = (self.state << 1) | b
        self.state &= (1 << 17) - 1
        return self.state

    def __iter__(self):
        return self
