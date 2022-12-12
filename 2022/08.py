def prepare_data(data, test=False):
    return [[int(d) for d in line] for line in data]


def resu1(data):
    resu = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            resu[(i, j)] = i == 0 or j == 0 or i == len(data) - 1 or j == len(data[i]) - 1 \
                           or data[i][j] > max(data[i][:j]) or data[i][j] > max(data[i][j + 1:]) \
                           or data[i][j] > max([v[j] for v in data[:i]]) \
                           or data[i][j] > max([v[j] for v in data[i + 1:]])
    return sum([int(v) for v in resu.values()])


def resu2(data):
    resu = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            left, right, up, down = 0, 0, 0, 0
            for v in reversed(data[i][:j]):
                left += 1
                if data[i][j] <= v:
                    break
            for v in data[i][j + 1:]:
                right += 1
                if data[i][j] <= v:
                    break
            for v in [v[j] for v in data[:i]][::-1]:
                up += 1
                if data[i][j] <= v:
                    break
            for v in [v[j] for v in data[i + 1:]]:
                down += 1
                if data[i][j] <= v:
                    break
            resu = max(resu, left * right * up * down)
    return resu


def test1(resu):
    return resu == 21


def test2(resu):
    return resu == 8


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
