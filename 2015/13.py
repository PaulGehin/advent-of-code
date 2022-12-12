def prepare_data(data, test=False):
    resu = dict()
    for line in data:
        splitted = line.split(" ")
        first, second, gain_sign, gain = splitted[0], splitted[-1][:-1], splitted[2], int(
            splitted[3])
        gain = gain if gain_sign == "gain" else -gain
        if not first in resu.keys():
            resu[first] = dict()
        resu[first][second] = gain
    return resu


def optimal_seating(attendees, data):
    if len(attendees) == 0:
        return optimal_seating(list(data.keys())[:1], data)
    elif len(attendees) == len(data):
        first, second = attendees[0], attendees[-1]
        return data[first][second] + data[second][first]
    else:
        resu = []
        for attendee in data:
            if not attendee in attendees:
                resu.append(data[attendees[-1]][attendee] + data[attendee]
                [attendees[-1]] + optimal_seating(attendees + [attendee], data))
        return max(resu)


def resu1(data):
    return optimal_seating([], data)


def resu2(data):
    attendees = list(data.keys())
    data["Santa"] = dict()
    for attendee in attendees:
        data["Santa"][attendee] = 0
        data[attendee]["Santa"] = 0
    return optimal_seating([], data)


def test1(resu):
    return resu == 330


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
