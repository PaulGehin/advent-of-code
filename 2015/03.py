def prepare_data(data, test=False):
    return data[0]


def new_position(position, direction):
    x, y = position
    if direction == "^":
        y += 1
    elif direction == "<":
        x -= 1
    elif direction == ">":
        x += 1
    elif direction == "v":
        y -= 1
    else:
        raise Exception()
    return (x, y)


def resu1(data):
    position = (0, 0)
    resu = {position}
    for direction in data:
        position = new_position(position, direction)
        resu.add(position)
    return len(resu)


def resu2(data):
    position = (0, 0)
    position_robot = (0, 0)
    resu = {position}
    for i, direction in enumerate(data):
        if i % 2 == 0:
            position = new_position(position, direction)
            resu.add(position)
        else:
            position_robot = new_position(position_robot, direction)
            resu.add(position_robot)
    return len(resu)


def test1(resu):
    return resu == 4


def test2(resu):
    return resu == 3


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
