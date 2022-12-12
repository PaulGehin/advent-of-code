import collections
import itertools


def prepare_data(data, test=False):
    data = "\n".join(data).split("\n\n")
    resu = dict()
    for tile in data:
        title, *grid = tile.split('\n')
        number = int(title.split()[1][:-1])
        resu[number] = grid
    return resu


def top(grid): return grid[0]


def bottom(grid): return grid[-1]


def left(grid): return ''.join(row[0] for row in grid)


def right(grid): return ''.join(row[-1] for row in grid)


def edges(grid): return top(grid), bottom(grid), left(grid), right(grid)


def flip_h(grid): return [row[::-1] for row in grid]


def flip_v(grid): return grid[::-1]


def rotate(grid):
    return [''.join(grid[i][j] for i in range(len(grid)))
            for j in range(len(grid[0]) - 1, -1, -1)]


def match_tiles(data):
    resu = collections.defaultdict(list)
    borders = borders = {
        'top': top,
        'bottom': bottom,
        'left': left,
        'right': right
    }

    for (i, grid_i), (j, grid_j) in itertools.combinations(data.items(), 2):
        for (side_i, f_i), (side_j, f_j) in itertools.product(borders.items(), borders.items()):
            border_i, border_j = f_i(grid_i), f_j(grid_j)
            if border_i == border_j:
                resu[i].append((side_i, False, j))
                resu[j].append((side_j, False, i))
                break
            if border_i[::-1] == border_j:
                resu[i].append((side_i, True, j))
                resu[j].append((side_j, True, i))
                break
    return resu


def compare_child_parent(grid_child, edges_parent, coord_parent):  # NOSONAR
    edges_child = edges(grid_child)
    top_parent, bottom_parent, left_parent, right_parent = edges_parent
    top_child, bottom_child, left_child, right_child = edges_child
    x, y = coord_parent
    resu = [coord_parent, grid_child]
    if top_child == bottom_parent:
        resu[0] = (x + 1, y)
        resu[1] = grid_child
    elif bottom_child == top_parent:
        resu[0] = (x - 1, y)
        resu[1] = grid_child
    elif left_child == right_parent:
        resu[0] = (x, y + 1)
        resu[1] = grid_child
    elif right_child == left_parent:
        resu[0] = (x, y - 1)
        resu[1] = grid_child

    elif bottom_parent == bottom_child:
        resu[0] = (x + 1, y)
        resu[1] = flip_v(grid_child)
    elif top_parent == top_child:
        resu[0] = (x - 1, y)
        resu[1] = flip_v(grid_child)
    elif right_parent == right_child:
        resu[0] = (x, y + 1)
        resu[1] = flip_h(grid_child)
    elif left_parent == left_child:
        resu[0] = (x, y - 1)
        resu[1] = flip_h(grid_child)

    elif bottom_parent == bottom_child[::-1]:
        resu[0] = (x + 1, y)
        resu[1] = rotate(rotate(grid_child))
    elif top_parent == top_child[::-1]:
        resu[0] = (x - 1, y)
        resu[1] = rotate(rotate(grid_child))
    elif right_parent == right_child[::-1]:
        resu[0] = (x, y + 1)
        resu[1] = rotate(rotate(grid_child))
    elif left_parent == left_child[::-1]:
        resu[0] = (x, y - 1)
        resu[1] = rotate(rotate(grid_child))

    elif bottom_parent == top_child[::-1]:
        resu[0] = (x + 1, y)
        resu[1] = flip_h(grid_child)
    elif top_parent == bottom_child[::-1]:
        resu[0] = (x - 1, y)
        resu[1] = flip_h(grid_child)
    elif right_parent == left_child[::-1]:
        resu[0] = (x, y + 1)
        resu[1] = flip_v(grid_child)
    elif left_parent == right_child[::-1]:
        resu[0] = (x, y - 1)
        resu[1] = flip_v(grid_child)

    elif bottom_parent == right_child:
        resu[0] = (x + 1, y)
        resu[1] = rotate(grid_child)
    elif top_parent == left_child:
        resu[0] = (x - 1, y)
        resu[1] = rotate(grid_child)
    elif right_parent == top_child[::-1]:
        resu[0] = (x, y + 1)
        resu[1] = rotate(grid_child)
    elif left_parent == bottom_child[::-1]:
        resu[0] = (x, y - 1)
        resu[1] = rotate(grid_child)

    elif bottom_parent == right_child[::-1]:
        resu[0] = (x + 1, y)
        resu[1] = flip_h(rotate(grid_child))
    elif top_parent == left_child[::-1]:
        resu[0] = (x - 1, y)
        resu[1] = flip_h(rotate(grid_child))
    elif right_parent == top_child:
        resu[0] = (x, y + 1)
        resu[1] = flip_v(rotate(grid_child))
    elif left_parent == bottom_child:
        resu[0] = (x, y - 1)
        resu[1] = flip_v(rotate(grid_child))

    elif bottom_parent == left_child:
        resu[0] = (x + 1, y)
        resu[1] = rotate(flip_h(grid_child))
    elif top_parent == right_child:
        resu[0] = (x - 1, y)
        resu[1] = rotate(flip_h(grid_child))
    elif right_parent == bottom_child[::-1]:
        resu[0] = (x, y + 1)
        resu[1] = flip_h(rotate(grid_child))
    elif left_parent == top_child[::-1]:
        resu[0] = (x, y - 1)
        resu[1] = flip_h(rotate(grid_child))

    elif bottom_parent == left_child[::-1]:
        resu[0] = (x + 1, y)
        resu[1] = rotate(rotate(rotate((grid_child))))
    elif top_parent == right_child[::-1]:
        resu[0] = (x - 1, y)
        resu[1] = rotate(rotate(rotate((grid_child))))
    elif right_parent == bottom_child:
        resu[0] = (x, y + 1)
        resu[1] = rotate(rotate(rotate((grid_child))))
    elif left_parent == top_child:
        resu[0] = (x, y - 1)
        resu[1] = rotate(rotate(rotate((grid_child))))
    return resu


def find_position_tiles(matches, data):
    start = [k for k, v in matches.items() if len(v) == 2][0]
    front = collections.deque([start])
    resu = {start: (0, 0)}
    grid = {start: data[start]}
    while front:
        parent = front.pop()
        grid_parent = grid[parent]
        edges_parent = edges(grid_parent)
        coord_parent = resu[parent]
        for _, _, child in matches[parent]:
            if child in resu:
                continue
            front.append(child)

            grid_child = data[child]
            resu[child], grid[child] = compare_child_parent(
                grid_child, edges_parent, coord_parent)

    return resu, grid, len(data[start])


def remove_borders(position, grid, n=10):
    (x_min, y_min), (x_max, y_max) = min(
        position.values()), max(position.values())

    pos = {}
    for k, p in position.items():
        pos[p] = k

    total = []
    for i in range(x_min, x_max + 1):
        row = []
        for j in range(y_min, y_max + 1):
            row.append(pos[i, j])
        total.append(row)

    resu = []
    for r in total:
        lines = [[] for _ in range(n - 2)]
        for c in r:
            for line, tile in zip(lines, grid[c][1:-1]):
                line += [*tile[1:-1]]
        resu += lines
    return resu


def find_monsters(grid):  # NOSONAR
    orientations = {
        'original': lambda g: g,
        'rotate': rotate,
        'rotate2': lambda g: rotate(rotate(g)),
        'rotate3': lambda g: rotate(rotate(rotate(g))),
        'flip_h': flip_h,
        'rotate_flip': lambda g: rotate(flip_h(g)),
        'rotate2_flip': lambda g: rotate(rotate(flip_h(g))),
        'rotate3_flip': lambda g: rotate(rotate(rotate(flip_h(g))))
    }
    monsters = collections.defaultdict(set)

    sea_monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   ',
    ]

    for name, f in orientations.items():
        oriented_grid = f(grid)
        for x in range(len(oriented_grid) - len(sea_monster) + 1):
            for y in range(len(oriented_grid[0]) - len(sea_monster[0]) + 1):
                maybe = set()
                ok = True
                for monster_x, monster_row in enumerate(sea_monster):
                    for monster_y, monster_character in enumerate(monster_row):
                        if monster_character == ' ':
                            continue
                        if oriented_grid[x + monster_x][y + monster_y] != '#':
                            ok = False
                            break
                        maybe.add((x + monster_x, y + monster_y))
                if ok:
                    monsters[name] |= maybe

    return ''.join(grid).count('#') - len([*monsters.values()][0])


def resu1(data):
    seen = collections.defaultdict(int)
    for tile in data:
        for edge in edges(data[tile]):
            seen[edge] += 1
            seen[edge[::-1]] += 1
    resu = 1
    for tile in data:
        tmp = 0
        for edge in edges(data[tile]):
            if seen[edge] == 1:
                tmp += 1
        if tmp == 2:
            resu *= tile
    return resu


def resu2(data):
    def arrange_tiles(data):
        return [*map(''.join, remove_borders(*find_position_tiles(match_tiles(data), data)))]

    return find_monsters(arrange_tiles(data))


def test1(resu):
    return resu == 20899048083289


def test2(resu):
    return resu == 273


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
