import math


def prepare_data(data, test=False):
    def prepare_line(line):
        action, value = line[0], int(line[1:])
        if action == "E":
            action = 0
        elif action == "N":
            action = math.pi / 2
        elif action == "W":
            action = math.pi
        elif action == "S":
            action = 3 * math.pi / 2
        elif action == "L":
            value = value * math.pi / 180
        elif action == "R":
            value = value * math.pi / 180
            action, value = "L", - value
        return action, value

    return list(map(prepare_line, data))


def travel(x, y, facing, action, value):
    if action == "F":
        return travel(x, y, facing, facing, value)
    elif action == "L":
        return x, y, (facing + value) % (2 * math.pi)
    else:
        return x + math.cos(action) * value, y + math.sin(action) * value, facing


def travel_with_waypoint(boat, waypoint, action, value):
    if action == "F":
        for _ in range(value):
            boat[0] += waypoint[0]
            boat[1] += waypoint[1]
    elif action == "L":
        waypoint = [math.cos(value) * waypoint[0] - math.sin(value) * waypoint[1],
                    math.sin(value) * waypoint[0] + math.cos(value) * waypoint[1]]
    else:
        waypoint[0] += math.cos(action) * value
        waypoint[1] += math.sin(action) * value
    return boat, waypoint


def resu1(data):
    resu = 0, 0, 0
    for line in data:
        resu = travel(resu[0], resu[1], resu[2], line[0], line[1])
    return abs(round(resu[0])) + abs(round(resu[1]))


def resu2(data):
    resu = [0, 0]
    waypoint = [10, 1]
    for line in data:
        resu, waypoint = travel_with_waypoint(resu, waypoint, line[0], line[1])
    return abs(round(resu[0])) + abs(round(resu[1]))


def test1(resu):
    return resu == 25


def test2(resu):
    return resu == 286


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
