def prepare_data(data, test=False):
    def prepare_line(line):
        foreign, english = line.split("(contains ")
        foreign = foreign.split()
        english = english[:-1].split(", ")
        return set(foreign), set(english)

    resu = list(map(prepare_line, data))
    return resu, define_allergens(resu)


def allergens_with_duplicates(data):
    resu = dict()
    for ingredients, allergens in data:
        for allergen in allergens:
            if allergen in resu.keys():
                resu[allergen] &= ingredients
            else:
                resu[allergen] = ingredients.copy()
    return resu


def remove_duplicates(resu):
    i, allergens = 0, list(resu.keys())
    while len(allergens) > 0:
        allergen = allergens[i % len(allergens)]
        if len(resu[allergen]) == 1:
            allergens.remove(allergen)
            for allergen_2 in allergens:
                resu[allergen_2] -= resu[allergen]
        i += 1
    return resu


def define_allergens(data):
    resu = allergens_with_duplicates(data)
    resu = remove_duplicates(resu)
    for key in resu:
        resu[key] = resu[key].pop()
    return resu


def resu1(data):
    data, allergens = data
    allergens = set(allergens.values())
    resu = 0
    for ingredients, _ in data:
        for ingredient in ingredients:
            if not ingredient in allergens:
                resu += 1
    return resu


def resu2(data):
    data, allergens = data
    resu = []
    for _, allergen in sorted(allergens.items(), key=lambda item: item[0]):
        resu.append(allergen)
    return ",".join(resu)


def test1(resu):
    return resu == 5


def test2(resu):
    return resu == "mxmxvkd,sqjhc,fvjkl"


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
