def prepare_data(data, test=False):
    if test:
        i = data.index("")
        return [data[:i], data[i + 1:]]
    return data


digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
reversed_digits = {k[::-1]: v for k, v in digits.items()}


def find_digit(line: str, catalog: dict[str, int] | None = None) -> int:
    catalog = {} if catalog is None else catalog
    for i, char in enumerate(line):
        if char.isdigit():
            return int(char)
        for k, v in catalog.items():
            if line[i:].startswith(k):
                return v


def resu1(data):
    if len(data) == 2:
        return sum(find_digit(line) * 10 + find_digit(line[::-1]) for line in data[0])
    return sum(find_digit(line) * 10 + find_digit(line[::-1]) for line in data)


def resu2(data):
    if len(data) == 2:
        return sum(find_digit(line, digits) * 10 + find_digit(line[::-1], reversed_digits) for line in data[1])
    return sum(find_digit(line, digits) * 10 + find_digit(line[::-1], reversed_digits) for line in data)


def test1(resu):
    return resu == 142


def test2(resu):
    return resu == 281


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
