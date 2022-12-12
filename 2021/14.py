from collections import Counter, defaultdict


def prepare_data(data, test=False):
    template, insertions = data[:data.index("")][0], list(
        map(lambda x: x.split(" -> "), data[data.index("") + 1:]))
    return template, insertions


def resu1(data):
    template, insertions = data
    resu = "" + template
    for _ in range(10):
        inserts = []
        for pair, insertion in insertions:
            for i in range(len(resu) - 1):
                if resu[i] + resu[i + 1] == pair:
                    inserts.append((i, insertion))
        inserts.sort(key=lambda x: x[0])
        while len(inserts) != 0:
            i, insertion = inserts.pop()
            resu = resu[:i + 1] + insertion + resu[i + 1:]
    counter = Counter()
    for c in resu:
        counter[c] += 1
    mc = counter.most_common()
    return mc[0][1] - mc[-1][1]


def resu2(data):
    template, pairs = data
    pair_insertions = {}
    for a, b in pairs:
        pair_insertions[(a[0], a[1])] = b

    pairs = defaultdict(int)
    for a, b in zip(template, template[1:]):
        pairs[(a, b)] += 1
    for _ in range(40):
        new_pairs = defaultdict(int)
        for pair, count in pairs.items():
            i = pair_insertions.get(pair, None)
            if i is not None:
                new_pairs[(pair[0], i)] += count
                new_pairs[(i, pair[1])] += count
            else:
                new_pairs[(pair[0], pair[1])] += count
        pairs = new_pairs
    counter = Counter()
    for (a, b), c in pairs.items():
        counter[a] += c
    counter[template[-1]] += 1
    mc = counter.most_common()
    return mc[0][1] - mc[-1][1]


def test1(resu):
    return resu == 1588


def test2(resu):
    return resu == 2188189693529


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
