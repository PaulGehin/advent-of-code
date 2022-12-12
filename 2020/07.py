def prepare_data(data, test=False):
    resu = {}
    for line in data:
        bag, contains = line.split(" contain ")
        bag = bag[:-5]
        resu[bag] = {}
        contains = contains.split(", ")
        for contain_bag in contains:
            if "no other bags" not in contain_bag:
                number = int(contain_bag.split(" ")[0])
                contain_bag = " ".join(contain_bag.split(" ")[1:-1])
                resu[bag][contain_bag] = number
    return resu


def resu1(data):
    def can_contains(bag):
        if bag in data.keys():
            if "shiny gold" in data[bag].keys():
                return True
            else:
                for key in data[bag].keys():
                    if can_contains(key):
                        return True
        return False

    return list(map(can_contains, data)).count(True)


def resu2(data):
    def sum_bags(bag, accumulator=0):
        if bag in data.keys():
            for key in data[bag].keys():
                accumulator += data[bag][key] + data[bag][key] * sum_bags(key)
        return accumulator

    return sum_bags("shiny gold")


def test1(resu):
    return resu == 4


def test2(resu):
    return resu == 32


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
