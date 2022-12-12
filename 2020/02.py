def prepare_data(data, test=False):
    return [(int(line.split(":")[0].split(" ")[0].split("-")[0]), int(line.split(":")[0].split(" ")[0].split("-")[1]),
             line.split(":")[0].split(" ")[1], line.split(":")[1].strip(" ")) for line in data]


def resu1(data):
    def verify_password(element):
        mini, maxi, character, password = element
        return password.count(character) in range(mini, maxi + 1)

    return list(map(verify_password, data)).count(True)


def resu2(data):
    def verify_password(element):
        first, second, character, password = element
        return (password[first - 1] + password[second - 1]).count(character) == 1

    return list(map(verify_password, data)).count(True)


def test1(resu):
    return resu == 2


def test2(resu):
    return resu == 1


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
