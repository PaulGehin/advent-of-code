def prepare_data(data, test=False):
    return list(map(int, data[0].split(",")))


# def resu1(data):
#     resu = data.copy()
#     resu.reverse()
#     for i in range(2020):
#         if i == len(resu):
#             if resu[0] in resu[1:]:
#                 resu.insert(0, resu[1:].index(resu[0]) + 1)
#             else:
#                 resu.insert(0, 0)
#     return resu[0]

def resu1(data):
    return age(data, 2020)


def age(data, number):
    resu = dict()
    last = 0
    for i in range(len(data)):
        resu[last] = i
        last = data[i]
    for i in range(len(data), number):
        if last in resu.keys():
            temp = last
            last = i - resu[last]
            resu[temp] = i
        else:
            resu[last] = i
            last = 0
    return last


def resu2(data):
    return age(data, 30000000)


def test1(resu):
    return resu == 436


def test2(resu):
    return resu == 175594


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
