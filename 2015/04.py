import hashlib


def prepare_data(data, test=False):
    return data[0]


def has_leading_zero(element, number=5):
    for character in element[:number]:
        if character != "0":
            return False
    return True


def md5_hash(element):
    return hashlib.md5(element.encode()).hexdigest()


def resu1(data):
    resu = 0
    while not has_leading_zero(md5_hash(f"{data}{resu}")):
        resu += 1
    return resu


def resu2(data):
    resu = 0
    while not has_leading_zero(md5_hash(f"{data}{resu}"), 6):
        resu += 1
    return resu


def test1(resu):
    return resu == 609043


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
