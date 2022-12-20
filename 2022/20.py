class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


def prepare_data(data, test=False):
    return [Number(int(i)) for i in data]


def mix(resu, data):
    for i in data:
        index = resu.index(i)
        new_index = (index + i.value) % (len(resu) - 1)
        resu.pop(index)
        resu.insert(new_index, i)


def resu1(data, mix_number=1):
    resu = data[:]
    zero, = [i for i in data if i.value == 0]

    for _ in range(mix_number):
        mix(data=data, resu=resu)

    zero_index = resu.index(zero)
    return sum([resu[(zero_index + i * 1_000) % len(resu)].value for i in [1, 2, 3]])


def resu2(data):
    return resu1(data=[Number(i.value * 811589153) for i in data], mix_number=10)


def test1(resu):
    return resu == 3


def test2(resu):
    return resu == 1623178306


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
