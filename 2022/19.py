import math
import re

from tqdm import tqdm


def prepare_data(data, test=False):
    def prepare_line(line):
        m = re.match(
            r"Blueprint ([0-9]+): Each ore robot costs ([0-9]+) ore. "
            r"Each clay robot costs ([0-9]+) ore. "
            r"Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay. "
            r"Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian.",
            line
        )
        return tuple(map(int, m.groups()))

    return [prepare_line(line) for line in data], test


def best_geodes(blueprint, time_limit):
    _, ore_ore, clay_ore, obs_ore, obs_clay, geode_ore, geode_obs = blueprint
    ore_robot_max_minute = time_limit - 6
    clay_robot_max_minute = time_limit - 4
    obs_robot_max_minute = time_limit - 2

    current_states = set()
    start = (1, 0, 0, 0, 1, 0, 0, 0)
    current_states.add(start)
    for minute in range(1, time_limit):
        next_states = set()
        for state in current_states:
            ore_rock, clay_rock, obs_rock, geode_rock, ore_robot, clay_robot, obs_robot, geode_robot = state
            next_states.add((ore_rock + ore_robot,
                             clay_rock + clay_robot,
                             obs_rock + obs_robot,
                             geode_rock + geode_robot,
                             ore_robot,
                             clay_robot,
                             obs_robot,
                             geode_robot))
            if ore_rock >= ore_ore and minute < ore_robot_max_minute:
                next_states.add((ore_rock + ore_robot - ore_ore,
                                 clay_rock + clay_robot,
                                 obs_rock + obs_robot,
                                 geode_rock + geode_robot,
                                 ore_robot + 1,
                                 clay_robot,
                                 obs_robot,
                                 geode_robot))
            if ore_rock >= clay_ore and minute < clay_robot_max_minute:
                next_states.add((ore_rock + ore_robot - clay_ore,
                                 clay_rock + clay_robot, obs_rock + obs_robot,
                                 geode_rock + geode_robot,
                                 ore_robot,
                                 clay_robot + 1,
                                 obs_robot,
                                 geode_robot))
            if ore_rock >= obs_ore and clay_rock >= obs_clay and minute < obs_robot_max_minute:
                next_states.add((ore_rock + ore_robot - obs_ore,
                                 clay_rock + clay_robot - obs_clay,
                                 obs_rock + obs_robot,
                                 geode_rock + geode_robot,
                                 ore_robot,
                                 clay_robot,
                                 obs_robot + 1,
                                 geode_robot))
            if ore_rock >= geode_ore and obs_rock >= geode_obs:
                next_states.add((ore_rock + ore_robot - geode_ore,
                                 clay_rock + clay_robot,
                                 obs_rock + obs_robot - geode_obs,
                                 geode_rock + geode_robot,
                                 ore_robot,
                                 clay_robot,
                                 obs_robot,
                                 geode_robot + 1))
        current_states = next_states
    return max(state[3] for state in current_states)


def resu1(data):
    data, test = data
    return sum(blueprint[0] * best_geodes(blueprint, 24) for blueprint in tqdm(data, desc=f"{test=}"))


def resu2(data):
    data, test = data
    if not test:
        data = data[:3]
    return math.prod(best_geodes(blueprint, 32) for blueprint in tqdm(data, desc=f"{test=}"))


def test1(resu):
    return resu == 33


def test2(resu):
    return resu == 56 * 62


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
