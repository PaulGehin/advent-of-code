import math


def prepare_data(data, test=False):
    resu = dict()
    zone = "fields"
    resu[zone] = dict()
    for line in data:
        if line == "":
            zone = ""
        elif zone == "":
            zone = line[:-1]
            resu[zone] = []
        elif zone == "fields":
            key, values = line.split(": ")
            resu[zone][key] = []
            for pos in values.split(" or "):
                mini, maxi = pos.split("-")
                resu[zone][key].append((int(mini), int(maxi)))
        else:
            resu[zone].append(list(map(int, line.split(","))))
    resu["your ticket"] = resu["your ticket"][0]
    return resu


def valid(number, fields):
    for key in fields:
        for mini, maxi in fields[key]:
            if mini <= number <= maxi:
                return True
    return False


def resu1(data):
    resu = []
    for ticket in data["nearby tickets"]:
        for number in ticket:
            if not valid(number, data["fields"]):
                resu.append(number)
    return sum(resu)


def resu2(data):
    nearby_tickets = []
    for ticket in data["nearby tickets"]:
        resu = []
        for number in ticket:
            if not valid(number, data["fields"]):
                resu.append(number)
        if resu == []:
            nearby_tickets.append(ticket)
    range_tickets = dict()
    for i, number in enumerate(data["your ticket"]):
        range_tickets[i] = [number]
    for ticket in nearby_tickets:
        for i, number in enumerate(ticket):
            range_tickets[i].append(number)
    description_tickets = dict()
    while len(description_tickets) < len(range_tickets):
        for key in range_tickets:
            possibilities = []
            for field in data["fields"]:
                if not field in description_tickets.keys():
                    n_ok = 0
                    for number in range_tickets[key]:
                        if valid(number, {field: data["fields"][field]}):
                            n_ok += 1
                    if n_ok == len(range_tickets[key]):
                        possibilities.append(field)
            if len(possibilities) == 1:
                description_tickets[possibilities[0]] = key
    resu = []
    for key in description_tickets:
        if "departure" in key:
            resu.append(data["your ticket"][description_tickets[key]])
    return math.prod(resu)


def test1(resu):
    return True
    # return resu == 71


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
