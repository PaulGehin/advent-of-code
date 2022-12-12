import random


def prepare_data(data, test=False):
    wires, digits = list(), list()
    resu = {"dataset": list()}
    for line in data:
        a, b = line.split(" | ")
        resu["dataset"].append([a.split(), b.split()])
        wires += a.split(' ')
        digits += b.split(' ')
    resu["wires"] = wires
    resu["digits"] = digits
    return resu


def resu1(data):
    resu = 0
    for digit in data["digits"]:
        if len(digit) in [2, 3, 4, 7]:
            resu += 1
    return resu


def resu2(data):
    resu = 0
    for help, value in data["dataset"]:
        pattern = dict()
        for digit in help:
            if digit not in pattern.keys() and len(digit) in [7]:
                pattern[digit] = "8"
            elif digit not in pattern.keys() and len(digit) in [2]:
                pattern[digit] = "1"
            elif digit not in pattern.keys() and len(digit) == 4:
                pattern[digit] = "4"
            elif digit not in pattern.keys() and len(digit) == 3:
                pattern[digit] = "7"
        for digit in help:
            if digit not in pattern.keys() and len(digit) == 5:
                count_1, count_4, count_7 = 0, 0, 0
                for c in digit:
                    for key in pattern.keys():
                        if c in key:
                            if pattern[key] == "1":
                                count_1 += 1
                            elif pattern[key] == "4":
                                count_4 += 1
                            elif pattern[key] == "7":
                                count_7 += 1
                if count_1 == 2 and count_4 == 3 and count_7 == 3:
                    pattern[digit] = "3"
                elif count_1 == 1 and count_4 == 2 and count_7 == 2:
                    pattern[digit] = "2"
                elif count_1 == 1 and count_4 == 3 and count_7 == 2:
                    pattern[digit] = "5"
                else:
                    print(digit)
            elif digit not in pattern.keys() and len(digit) == 6:
                count_1, count_4, count_7 = 0, 0, 0
                for c in digit:
                    for key in pattern.keys():
                        if c in key:
                            if pattern[key] == "1":
                                count_1 += 1
                            elif pattern[key] == "4":
                                count_4 += 1
                            elif pattern[key] == "7":
                                count_7 += 1
                if count_1 == 2 and count_4 == 3 and count_7 == 3:
                    pattern[digit] = "0"
                elif count_1 == 1 and count_4 == 3 and count_7 == 2:
                    pattern[digit] = "6"
                elif count_1 == 2 and count_4 == 4 and count_7 == 3:
                    pattern[digit] = "9"
                else:
                    print(digit)
        number = ""
        for digit in value:
            true_digit = digit
            while true_digit not in pattern.keys():
                true_digit = ''.join(random.sample(
                    true_digit, len(true_digit)))
            number += pattern[true_digit]
        resu += int(number)
    return resu


def test1(resu):
    return resu == 26


def test2(resu):
    return resu == 61229


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
