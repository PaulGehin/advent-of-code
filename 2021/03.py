def prepare_data(data, test=False):
    return data


def resu1(data):
    gamma, epsilon = "", ""
    n = len(data[0])
    for i in range(n):
        one_most_common = 0
        for line in data:
            if line[i] == '1':
                one_most_common += 1
        if one_most_common > len(data) // 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def oxygen(data, position=0):
    if len(data) == 1:
        return int(data[0], 2)
    one_most_common = 0
    for line in data:
        if line[position] == '1':
            one_most_common += 1
    new_data = list()
    if one_most_common > len(data) // 2 or (one_most_common == len(data) // 2 and len(data) % 2 == 0):
        for line in data:
            if line[position] == '1':
                new_data.append(line)
    else:
        for line in data:
            if line[position] == '0':
                new_data.append(line)
    return oxygen(new_data, position + 1)


def co2(data, position=0):
    if len(data) == 1:
        return int(data[0], 2)
    one_most_common = 0
    for line in data:
        if line[position] == '1':
            one_most_common += 1
    new_data = list()
    if one_most_common > len(data) // 2 or (one_most_common == len(data) // 2 and len(data) % 2 == 0):
        for line in data:
            if line[position] == '0':
                new_data.append(line)
    else:
        for line in data:
            if line[position] == '1':
                new_data.append(line)
    return co2(new_data, position + 1)


def resu2(data):
    return oxygen(data) * co2(data)


def test1(resu):
    return resu == 198


def test2(resu):
    return resu == 230


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
