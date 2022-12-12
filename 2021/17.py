def prepare_data(data, test=False):
    data = data[0]
    x, y = data[data.index("x"):].split(',')
    x = x.split("x=")[1].split("..")
    y = y.split("y=")[1].split("..")
    return compute([[int(k) for k in x], [int(k) for k in y]])


def compute(data):
    target_x, target_y = data
    min_x, max_x = target_x
    min_y, max_y = target_y
    highest_y = 0
    matches = set()
    for velocity_y in range(min_y, -min_y):
        for velocity_x in range(max_x + 1):
            position = (0, 0)
            velocity = (velocity_y, velocity_x)
            y_max = 0
            while not (min_x <= position[1] <= max_x and min_y <= position[0] <= max_y) and position[0] >= min_y and \
                    position[1] <= max_x:
                position = (position[0] + velocity[0],
                            position[1] + velocity[1])
                y_max = max((y_max, position[0]))
                velocity = (velocity[0] - 1, max(0, velocity[1] - 1))
            if min_x <= position[1] <= max_x and min_y <= position[0] <= max_y:
                matches.add((velocity_y, velocity_x))
                highest_y = max((highest_y, y_max))
    return [highest_y, len(matches)]


def resu1(resu):
    return resu[0]


def resu2(resu):
    return resu[1]


def test1(resu):
    return resu == 45


def test2(resu):
    return resu == 112


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
