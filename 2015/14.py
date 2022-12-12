import copy
import itertools
import re
from typing import Iterator


class Deer:
    def __init__(self, name: str, speed: int, active_time: int, rest_time: int):
        self.name = name
        self.speed = speed
        self.active_time = active_time
        self.rest_time = rest_time
        self.position = 0
        self.points = 0
        self._seq = self._sequence()

    def __repr__(self):
        return str(self.__dict__)

    def _sequence(self) -> Iterator[int]:
        move = itertools.repeat(self.speed, self.active_time)
        rest = itertools.repeat(0, self.rest_time)
        return itertools.cycle(itertools.chain(move, rest))

    def move(self):
        self.position += next(self._seq)


def prepare_data(data, test=False):
    parser = re.compile(
        r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds"
    )

    def prepare_line(line):
        match = re.search(parser, line)
        if not match:
            raise ValueError("Can't parse line")
        (name, speed, active_time, rest_time) = match.group(1, 2, 3, 4)
        return Deer(name, int(speed), int(active_time), int(rest_time))

    return list(map(prepare_line, data))


def race_winner_distance(deers, end):
    deers = copy.deepcopy(deers)
    for _ in range(end):
        for deer in deers:
            deer.move()
    winner = max(deers, key=lambda deer: deer.position)
    return winner.position


def race_winner_points(deers, end):
    deers = copy.deepcopy(deers)
    for _ in range(end):
        for deer in deers:
            deer.move()
        leader = max(deers, key=lambda deer: deer.position)
        leaders = [deer for deer in deers if deer.position == leader.position]
        for leader in leaders:
            leader.points += 1

    winner = max(deers, key=lambda deer: deer.points)
    return winner.points


def resu1(data):
    end = 1000 if len(data) == 2 else 2503
    return race_winner_distance(data, end)


def resu2(data):
    end = 1000 if len(data) == 2 else 2503
    return race_winner_points(data, end)


def test1(resu):
    return resu == 1120


def test2(resu):
    return resu == 689


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
