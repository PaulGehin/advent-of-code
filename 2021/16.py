import math


def prepare_data(data, test=False):
    return Packet(str(bin(int("".join(data), 16)))[2:])


class Packet:
    def __init__(self, transmission=None):
        self.V = 0
        self.T = 0
        self.literal = None
        self.subpackets = list()

        i = 0
        self.V = int(transmission[i:i + 3], 2)
        i += 3
        self.T = int(transmission[i:i + 3], 2)
        i += 3
        if self.T == 4:
            self.literal = 0
            last_group = 1
            while last_group != 0:
                last_group = int(transmission[i:i + 1], 2)
                i += 1
                self.literal <<= 4
                self.literal |= int(transmission[i:i + 4], 2)
                i += 4
        else:
            I = int(transmission[i:i + 1], 2)
            i += 1
            if I == 0:
                L = int(transmission[i:i + 15], 2)
                i += 15
                subpackets_length = 0
                while subpackets_length < L:
                    subpacket = Packet(transmission[i:])
                    i += subpacket.length
                    subpackets_length += subpacket.length
                    self.subpackets.append(subpacket)
            else:
                num_subpackets = int(transmission[i:i + 11], 2)
                i += 11
                for _ in range(num_subpackets):
                    subpacket = Packet(transmission[i:])
                    i += subpacket.length
                    self.subpackets.append(subpacket)
        self.length = i

    def version_sum(self):
        return self.V + sum(subpacket.version_sum() for subpacket in self.subpackets)

    def evaluate(self):
        if self.T == 0:
            return sum(subpacket.evaluate() for subpacket in self.subpackets)
        elif self.T == 1:
            return math.prod(subpacket.evaluate() for subpacket in self.subpackets)
        elif self.T == 2:
            return min(subpacket.evaluate() for subpacket in self.subpackets)
        elif self.T == 3:
            return max(subpacket.evaluate() for subpacket in self.subpackets)
        elif self.T == 4:
            return self.literal
        elif self.T == 5:
            return 1 if self.subpackets[0].evaluate() > self.subpackets[1].evaluate() else 0
        elif self.T == 6:
            return 1 if self.subpackets[0].evaluate() < self.subpackets[1].evaluate() else 0
        elif self.T == 7:
            return 1 if self.subpackets[0].evaluate() == self.subpackets[1].evaluate() else 0
        else:
            raise ValueError(f"T value not found : {self.T}")


def resu1(data):
    return data.version_sum()


def resu2(data):
    return data.evaluate()


def test1(resu):
    return resu == 31


def test2(resu):
    return resu == 54


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
