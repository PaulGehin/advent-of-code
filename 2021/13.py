def prepare_data(data, test=False):
    points, instructions = data[:data.index("")], data[data.index("") + 1:]
    return (points, instructions)


def resu1(data):
    coords = set()
    points, instructions = data
    for line in points:
        x_s, y_s = line.split(',')
        coords.add((int(x_s), int(y_s)))

    for line in instructions:
        start, end = line.split('=')
        direction = start[-1]
        value = int(end)

        if direction == 'x':
            coords = {
                (
                    x if x < value else value - (x - value),
                    y
                )
                for x, y in coords
            }
        else:
            coords = {
                (
                    x,
                    y if y < value else value - (y - value),
                )
                for x, y in coords
            }

        break

    return len(coords)


def resu2(data):
    coords = set()

    points, instructions = data

    for line in points:
        x_s, y_s = line.split(',')
        coords.add((int(x_s), int(y_s)))

    for line in instructions:
        start, end = line.split('=')
        direction = start[-1]
        value = int(end)

        if direction == 'x':
            coords = {
                (
                    x if x < value else value - (x - value),
                    y
                )
                for x, y in coords
            }
        else:
            coords = {
                (
                    x,
                    y if y < value else value - (y - value),
                )
                for x, y in coords
            }

    max_x = max(x for x, _ in coords)
    max_y = max(y for _, y in coords)

    print('\n'.join(
        ''.join(
            '#' if (x, y) in coords else ' '
            for x in range(max_x + 1)
        )
        for y in range(max_y + 1)
    ))
    return None


def test1(resu):
    return resu == 17


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
