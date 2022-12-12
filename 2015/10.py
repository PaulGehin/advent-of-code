def prepare_data(data, test=False):
    return data[0]


def look(word):
    resu, character = [], ""
    for c in word:
        if c == character:
            resu[-1][-1] += 1
        else:
            resu.append([c, 1])
        character = c
    return resu


def say(sequence):
    return "".join([str(j) + str(i) for i, j in sequence])


def look_and_say(word):
    return say(look(word))


def resu1(data):
    resu = data
    for _ in range(40):
        resu = look_and_say(resu)
    return len(resu)


def resu2(data):
    resu = data
    for _ in range(50):
        resu = look_and_say(resu)
    return len(resu)


def test1(resu):
    return True


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
