def prepare_data(data, test=False):
    return [x.split(" ") for x in data]


def score_me(a, x):
    resu = 0
    match x:
        case "X":
            resu += 1
        case "Y":
            resu += 2
        case "Z":
            resu += 3
    if a == "A" and x == "X" or a == "B" and x == "Y" or a == "C" and x == "Z":
        resu += 3
    elif a == "A" and x == "Y" or a == "B" and x == "Z" or a == "C" and x == "X":
        resu += 6
    return resu


def score_me_2(a, x):
    resu = 0
    match x:
        case "Y":
            resu += 3
        case "Z":
            resu += 6
    if a == "A" and x == "Y" or a == "B" and x == "X" or a == "C" and x == "Z":
        resu += 1
    elif a == "A" and x == "Z" or a == "B" and x == "Y" or a == "C" and x == "X":
        resu += 2
    elif a == "A" and x == "X" or a == "B" and x == "Z" or a == "C" and x == "Y":
        resu += 3
    return resu


def resu1(data):
    return sum(score_me(a, b) for a, b in data)


def resu2(data):
    return sum(score_me_2(a, b) for a, b in data)


def test1(resu):
    return resu == 15


def test2(resu):
    return resu == 12


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
