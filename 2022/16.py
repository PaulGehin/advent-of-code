import re
from collections import defaultdict

from networkx import Graph, shortest_path_length


def prepare_data(data, test=False):
    graph = Graph()
    rates = {"AA": 0}
    valves = {}
    for line in data:
        m = re.match(r"Valve (.*) has flow rate=(\d*); tunnels? leads? to valves? (.*)", line)
        valve, rate, tunnels = m.groups()
        rate = int(rate)
        tunnels = [tunnel.strip() for tunnel in tunnels.split(',')]

        if rate > 0:
            rates[valve] = rate
        graph.add_node(valve)
        for tunnel in tunnels:
            graph.add_edge(valve, tunnel)

        open_valve_name = valve.lower()
        valves[valve] = {'rate': 0, 'destinations': tunnels + [open_valve_name]}
        valves[open_valve_name] = {'rate': rate, 'destinations': tunnels}

    resu = defaultdict(list)
    for valve in rates:
        for tunnel in rates:
            resu[valve].append((tunnel, shortest_path_length(graph, valve, tunnel) + 1))

    return resu, rates, valves


def compute(my_position, elephant_position, my_travel, elephant_travel, graph, rates, visited, score, minutes):
    if minutes == 0:
        return score

    if my_travel > 0 and elephant_travel > 0:
        return compute(
            my_position, elephant_position, my_travel - 1, elephant_travel - 1, graph, rates, visited, score, minutes - 1
        )

    best = score
    if my_travel == 0:
        found = False
        for destination, distance in graph[my_position]:
            if distance >= minutes or destination in visited:
                continue
            found = True
            visited.add(destination)
            result = compute(
                destination,
                elephant_position,
                distance,
                elephant_travel,
                graph,
                rates,
                visited,
                score + rates[destination] * (minutes - distance),
                minutes,
            )
            visited.remove(destination)
            if result > best:
                best = result
        if found:
            return best

    if elephant_travel == 0:
        for destination, distance in graph[elephant_position]:
            if distance >= minutes or destination in visited:
                continue
            visited.add(destination)
            result = compute(
                my_position,
                destination,
                my_travel,
                distance,
                graph,
                rates,
                visited,
                score + rates[destination] * (minutes - distance),
                minutes,
            )
            visited.remove(destination)
            if result > best:
                best = result

    return best


def resu1(data):
    graph, rates, _ = data
    return compute("AA", "AA", 0, 100, graph, rates, {"AA"}, 0, 30)


def search(valves, paths, path, minutes, depth):
    if depth == 0:
        return
    my_path = path[0]
    elephant_path = path[1]
    my_destinations = valves[my_path[-2:]]['destinations']
    elephant_destinations = valves[elephant_path[-2:]]['destinations']
    score = paths[path]
    for my_dest in my_destinations:
        for elephant_dest in elephant_destinations:
            my_dest_is_open_and_in_either_path = my_dest.islower() and (my_dest in my_path or my_dest in elephant_path)
            elephant_dest_is_open_and_in_either_path = \
                elephant_dest.islower() and (elephant_dest in my_path or elephant_dest in elephant_path)
            if not (my_dest == elephant_dest
                    or my_dest_is_open_and_in_either_path
                    or elephant_dest_is_open_and_in_either_path):
                new_path = (my_path + my_dest, elephant_path + elephant_dest)
                if new_path not in paths:
                    rate_at_my_dest = valves[my_dest]['rate']
                    rate_at_elephant_dest = valves[elephant_dest]['rate']
                    my_score = rate_at_my_dest * (minutes - 1)
                    elephant_score = rate_at_elephant_dest * (minutes - 1)
                    paths[new_path] = score + my_score + elephant_score
                    search(valves, paths, new_path, minutes - 1, depth - 1)


def resu2(data):
    graph, rates, valves = data

    # Takes forever and the result is wrong...
    # return compute("AA", "AA", 0, 0, graph, rates, {"AA"}, 0, 26)

    path_start = ('AA', 'AA')
    minutes = 26
    cut_tree = 25_000  # arbitrary
    paths = {path_start: 0}

    while minutes > 0:
        best_paths = sorted(paths, key=paths.get, reverse=True)[:cut_tree]
        paths = {path: paths[path] for path in best_paths}
        for path in list(paths.keys()):
            search(valves, paths, path, minutes, 1)
        minutes -= 1
    best_paths = sorted(paths, key=paths.get, reverse=True)[:cut_tree]
    return paths[best_paths[0]]


def test1(resu):
    return resu == 1651


def test2(resu):
    return resu == 1707


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
