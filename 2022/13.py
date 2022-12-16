from functools import cmp_to_key


def prepare_data(data, test=False):
    resu = []
    for i, pair in enumerate('\n'.join(data).split('\n\n')):
        p1, p2 = pair.splitlines()
        p1, p2 = map(eval, (p1, p2))
        resu.append((p1, p2))
    return resu


def cmp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a < b
    if isinstance(a, list) and isinstance(b, list):
        for i in range(len(a)):
            if i >= len(b):
                return False
            if cmp(a[i], b[i]):
                return True
            if cmp(b[i], a[i]):
                return False
            pass
        return len(a) < len(b)
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]
    return cmp(a, b)


def resu1(data):
    return sum(i + 1 if cmp(p1, p2) else 0 for i, (p1, p2) in enumerate(data))


def resu2(data):
    packets = []
    for p1, p2 in data:
        packets.append(p1)
        packets.append(p2)
    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key=cmp_to_key(lambda a, b: -1 if cmp(a, b) else cmp(b, a)))

    divider_packet = 0
    for i, packet in enumerate(packets):
        if packet == [[2]]:
            divider_packet = i + 1
            continue
        if packet == [[6]]:
            return divider_packet * (i + 1)


def test1(resu):
    return resu == 13


def test2(resu):
    return resu == 140


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
