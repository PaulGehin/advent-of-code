import copy


def prepare_data(data, test=False):
    data = "\n".join(data).split("\n\n")
    player_1 = [int(x) for x in data[0].split('\n')[1:]]
    player_2 = [int(x) for x in data[1].split('\n')[1:]]
    return player_1, player_2


def combat_round(deck_1, deck_2):
    card_1 = deck_1.pop(0)
    card_2 = deck_2.pop(0)
    if card_1 > card_2:
        deck_1.append(card_1)
        deck_1.append(card_2)
    elif card_1 < card_2:
        deck_2.append(card_2)
        deck_2.append(card_1)


def count_points(deck):
    resu = 0
    n = len(deck)
    for i, card in enumerate(deck):
        resu += (n - i) * card
    return resu


def recursive_combat(deck_1, deck_2):
    seen = seen = set()
    while len(deck_1) != 0 and len(deck_2) != 0:
        if (tuple(deck_1), tuple(deck_2)) in seen:
            return 1
        seen.add((tuple(deck_1), tuple(deck_2)))
        card_1 = deck_1.pop(0)
        card_2 = deck_2.pop(0)
        if card_1 <= len(deck_1) and card_2 <= len(deck_2):
            winner = recursive_combat(
                copy.copy(deck_1[:card_1]), copy.copy(deck_2[:card_2]))
        elif card_1 > card_2:
            winner = 1
        else:
            winner = 2
        if winner == 1:
            deck_1.append(card_1)
            deck_1.append(card_2)
        else:
            deck_2.append(card_2)
            deck_2.append(card_1)
    if len(deck_1) == 0:
        return 2
    else:
        return 1


def resu1(data):
    player_1, player_2 = data
    deck_1 = copy.copy(player_1)
    deck_2 = copy.copy(player_2)
    while len(deck_1) > 0 and len(deck_2) > 0:
        combat_round(deck_1, deck_2)
    if len(deck_1) == 0:
        return count_points(deck_2)
    else:
        return count_points(deck_1)


def resu2(data):
    player_1, player_2 = data
    deck_1 = copy.copy(player_1)
    deck_2 = copy.copy(player_2)
    winner = recursive_combat(deck_1, deck_2)
    if winner == 1:
        return count_points(deck_1)
    else:
        return count_points(deck_2)


def test1(resu):
    return resu == 306


def test2(resu):
    return resu == 291


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
