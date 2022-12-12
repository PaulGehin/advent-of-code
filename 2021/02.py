def prepare_data(data, test=False):
    return data


def resu1(data):
    depth, position = 0, 0
    for line in data:
        command, units = line.split()
        units = int(units)
        if command == "forward":
            position += units
        elif command == "down":
            depth += units
        elif command == "up":
            depth -= units
    return depth * position


def resu2(data):
    depth, position, aim = 0, 0, 0
    for line in data:
        command, units = line.split()
        units = int(units)
        if command == "forward":
            position += units
            depth += aim * units
        elif command == "down":
            aim += units
        elif command == "up":
            aim -= units
    return depth * position


def test1(resu):
    return resu == 150


def test2(resu):
    return resu == 900


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
