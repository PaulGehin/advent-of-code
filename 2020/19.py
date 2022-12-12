def prepare_data(data, test=False):
    resu, is_rule = dict(), True
    resu["rules"] = dict()
    resu["messages"] = []
    for line in data:
        if line == "":
            is_rule = False
        elif is_rule:
            key, value = line.split(": ")
            value = value.strip("\"")
            resu["rules"][key] = value.split()
        else:
            resu["messages"].append(line)
    return resu


def decode_rule(line, rules):
    if "|" in line:
        i = line.index("|")
        return [[decode_rule(line[:i], rules), decode_rule(line[i + 1:], rules)]]
    else:
        resu = []
        for rule in line:
            if rule.isnumeric():
                resu.extend(decode_rule(rules[rule], rules))
            else:
                resu.append(rule)
        return resu


def valid(message, rules):
    n = len(message)
    if n == 0 and len(rules) != 0:
        return -1
    i = 0
    for j, rule in enumerate(rules):
        if type(rule) == type(list()):
            for sub_rule in rule:
                temp = valid(message[i:], sub_rule + rules[j + 1:])
                if temp + i == n:
                    return n
            return -1
        else:
            if message[i] == rule:
                i += 1
            else:
                return -1
    return i


def resu1(data):
    rule_0 = decode_rule(data["rules"]["0"], data["rules"])

    def valid_message(message):
        return valid(message, rule_0) == len(message)

    return list(map(valid_message, data["messages"])).count(True)


def resu2(data):
    data["rules"]["8"] = ["42"]
    data["rules"]["11"] = ["42", "31"]
    for i in range(2, 21):
        data["rules"]["8"].extend(["|"] + ["42" for _ in range(i)])
        data["rules"]["11"].extend(
            ["|"] + ["42" for _ in range(i)] + ["31" for _ in range(i)])
    return resu1(data)


def test1(resu):
    return resu == 2


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
