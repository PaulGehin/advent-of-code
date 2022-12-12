from math import prod


def prepare_data(data, test=False):
    return list(map(lambda x: x.strip(), data))


def left_to_right(expression):
    resu, first, operator = None, True, None
    for elem in expression.split():
        if elem.isnumeric():
            if first:
                resu = int(elem)
                first = False
            elif operator == "+":
                resu += int(elem)
            else:
                resu *= int(elem)
        else:
            operator = elem
    return resu


def add_over_mul(expression):
    resu, temp, operator = [], 1, "*"
    for elem in expression.split():
        if elem.isnumeric():
            if operator == "+":
                temp += int(elem)
            else:
                resu.append(temp)
                temp = int(elem)
        else:
            operator = elem
    resu.append(temp)
    return prod(resu)


def my_eval(line, precedence=left_to_right):
    if "(" in line:
        start = line.rindex("(")
        end = line.find(")", start)
        line = line[:start] + \
               str(precedence(line[start + 1:end])) + \
               line[end + 1:]
        return my_eval(line, precedence)
    return precedence(line)


def resu1(data):
    return sum(map(my_eval, data))


def resu2(data):
    return sum(map(lambda line: my_eval(line, add_over_mul), data))


def test1(resu):
    return resu == 71 + 51


def test2(resu):
    return resu == 231 + 51


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
