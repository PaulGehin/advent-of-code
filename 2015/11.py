def prepare_data(data, test=False):
    return data[0]


def next_letter(letter):
    return "a" if letter == "z" else chr(ord(letter) + 1)


def increasing_straight(word):
    if len(word) < 3:
        return False
    else:
        first = word[0]
        second = next_letter(first)
        third = next_letter(second)
        return ord(first) < ord("y") and second == word[1] and third == word[2] or increasing_straight(word[1:])


def do_contain(word, characters):
    return False if len(characters) == 0 else characters[0] in word or do_contain(word, characters[1:])


def number_pair(word):
    if len(word) < 2:
        return 0
    elif word[0] == word[1]:
        return 1 + number_pair(word[2:])
    else:
        return number_pair(word[1:])


def is_valid(word):
    return increasing_straight(word) and not do_contain(word, ["i", "o", "l"]) and number_pair(word) > 1


def not_contain(word, characters):
    if len(word) == 0:
        return word
    elif word[0] in characters:
        resu = word[0]
        for c in characters:
            resu = resu.replace(c, next_letter(c))
        resu += "".join(["a" for _ in range(len(word) - 1)])
        return resu
    else:
        return word[0] + not_contain(word[1:], characters)


def next_word(word):
    word = not_contain(word, ["i", "o", "l"])
    resu = next_letter(word[-1])
    return next_word(word[:-1]) + resu if resu == "a" else word[:-1] + resu


def resu1(data):
    data = next_word(data)
    while not is_valid(data):
        data = next_word(data)
    return data


def resu2(data):
    data = resu1(data)
    return resu1(data)


def test1(resu):
    return resu == "ghjaabcc"


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
