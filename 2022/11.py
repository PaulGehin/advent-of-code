import collections
import copy
import math
import re


def prepare_monkey(section):
    monkey = {}
    lines = section.split('\n')
    match = re.search(r'^ {2}Starting items: (\d+(?:, \d+)*)$', lines[1])
    monkey['items'] = collections.deque(map(int, match.group(1).split(', ')))
    match = re.search(r'^ {2}Operation: new = old ([+*]) (\d+|old)$', lines[2])
    monkey['op'] = match.group(1)
    monkey['op_num'] = match.group(2)
    if monkey['op_num'].isdigit():
        monkey['op_num'] = int(monkey['op_num'])
    match = re.search(r'^ {2}Test: divisible by (\d+)$', lines[3])
    monkey['test'] = int(match.group(1))
    match = re.search(r'^ {4}If true: throw to monkey (\d+)$', lines[4])
    if_true = int(match.group(1))
    match = re.search(r'^ {4}If false: throw to monkey (\d+)$', lines[5])
    if_false = int(match.group(1))
    monkey['next'] = [if_false, if_true]
    return monkey


def prepare_data(data, test=False):
    return [prepare_monkey(section) for section in ('\n'.join(data)).split('\n\n')]


def do_round(monkeys, mod=None):
    for monkey in monkeys:
        while monkey['items']:
            monkey['inspections'] = monkey.get('inspections', 0) + 1
            worry = monkey['items'].popleft()
            op_num = monkey['op_num']
            if op_num == 'old':
                op_num = worry
            if monkey['op'] == '+':
                worry += op_num
            elif monkey['op'] == '*':
                worry *= op_num
            if mod:
                worry %= mod
            else:
                worry //= 3
            thrown = monkey['next'][worry % monkey['test'] == 0]
            monkeys[thrown]['items'].append(worry)


def resu1(data, mod=None, n_round=20):
    monkeys = copy.deepcopy(data)
    for _ in range(n_round):
        do_round(monkeys, mod)
    inspections = sorted((monkey['inspections'] for monkey in monkeys), reverse=True)
    return inspections[0] * inspections[1]


def resu2(data):
    return resu1(data, mod=math.prod(monkey['test'] for monkey in data), n_round=10_000)


def test1(resu):
    return resu == 10605


def test2(resu):
    return resu == 2713310158


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
