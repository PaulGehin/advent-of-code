def prepare_data(data, test=False):
    rock_data = """
                ####
                
                .#.
                ###
                .#.
                
                ..#
                ..#
                ###
                
                #
                #
                #
                #
                
                ##
                ##
                """.strip().split("\n\n")
    rocks = []
    rocks_height = []
    for rock in rock_data:
        current_rock = []
        row = 0
        for line in rock.strip().split("\n"):
            for column, char in enumerate(line.strip()):
                if char == "#":
                    current_rock.append((row, column))
            row -= 1
        rocks.append(current_rock)
        rocks_height.append(-row + 1)

    return [character == "<" for character in data[0]], rocks, rocks_height


def check_rock(filled, rock, row, column):
    for coord in rock:
        if coord[0] + row <= 0:
            return False
        if not 0 <= coord[1] + column < 7:
            return False
        if (coord[0] + row, coord[1] + column) in filled:
            return False
    return True


def fall(current, filled, i, jetstream, resu, rocks, rocks_height):
    rock = rocks[i % 5]
    row = resu + rocks_height[i % 5] + 2
    column = 2
    while True:
        is_pushing_left = jetstream[current % len(jetstream)]
        current += 1
        if is_pushing_left and check_rock(filled, rock, row, column - 1):
            column -= 1
        elif not is_pushing_left and check_rock(filled, rock, row, column + 1):
            column += 1
        if not check_rock(filled, rock, row - 1, column):
            break
        row -= 1
    for coord in rock:
        filled.add((coord[0] + row, coord[1] + column))
        resu = max(resu, coord[0] + row)
    return current, resu


def resu1(data):
    jetstream, rocks, rocks_height = data
    resu = 0
    filled = set()
    current = 0
    for i in range(2022):
        current, resu = fall(current, filled, i, jetstream, resu, rocks, rocks_height)
    return resu


def resu2(data):
    jetstream, rocks, rocks_height = data
    resu = 0
    skipped_resu = 0
    filled = set()
    current = 0
    hist = {}
    i = 0
    time_skipping = True
    target = 1000000000000
    while i < target:
        current, resu = fall(current, filled, i, jetstream, resu, rocks, rocks_height)
        if i > 2022 and time_skipping:
            if (i % 5, current % len(jetstream)) in hist:
                x = hist[i % 5, current % len(jetstream)]
                drops = i - x[1]
                cycles = (target - i) // drops
                i += cycles * drops + 1
                skipped_resu = (resu - x[0]) * cycles
                time_skipping = False
                continue
            hist[i % 5, current % len(jetstream)] = (resu, i)
        i += 1
    return resu + skipped_resu


def test1(resu):
    return resu == 3068


def test2(resu):
    return resu == 1514285714288


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
