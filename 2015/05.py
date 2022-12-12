def prepare_data(data, test=False):
    return data


def do_contain(word, vowels=["a", "e", "i", "o", "u"], times=3):
    return sum(map(lambda vowel: word.count(vowel), vowels)) >= times


def two_letter(word, lap=1):
    for i in range(len(word) - lap):
        if word[i] == word[i + lap]:
            return True
    return False


def do_not_contain(word, possibilities=["ab", "cd", "pq", "xy"]):
    return sum(map(lambda possibility: word.count(possibility), possibilities)) == 0


def contain_pair(word):
    for i in range(len(word) - 3):
        if word[i:i + 2] in word[i + 2:]:
            return True
    return False


def resu1(data):
    def is_nice(word):
        return do_contain(word) and two_letter(word) and do_not_contain(word)

    return list(map(is_nice, data)).count(True)


def resu2(data):
    def is_nice(word):
        return two_letter(word, 2) and contain_pair(word)

    return list(map(is_nice, data)).count(True)


def test1(resu):
    return resu == 2


def test2(resu):
    return resu == 2


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
