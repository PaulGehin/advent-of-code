def prepare_data(data, test=False):
    return data


def resu1(data):
    table = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    resu = 0
    for line in data:
        expected = list()
        for c in line:
            if c == '(':
                expected.append(')')
            elif c == '[':
                expected.append(']')
            elif c == '{':
                expected.append('}')
            elif c == '<':
                expected.append('>')
            elif c == expected[-1]:
                expected = expected[:-1]
            else:
                resu += table[c]
                break
    return resu


def resu2(data):
    table = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    resu = list()
    for line in data:
        corrupted = False
        expected = list()
        for c in line:
            if c == '(':
                expected.append(')')
            elif c == '[':
                expected.append(']')
            elif c == '{':
                expected.append('}')
            elif c == '<':
                expected.append('>')
            elif c == expected[-1]:
                expected = expected[:-1]
            else:
                corrupted = True
                break
        if not corrupted:
            score = 0
            expected.reverse()
            for c in expected:
                score *= 5
                score += table[c]
            resu.append(score)
    resu.sort()
    return resu[len(resu) // 2]


def test1(resu):
    return resu == 26397


def test2(resu):
    return resu == 288957


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
