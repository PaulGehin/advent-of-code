def prepare_data(data, test=False):
    return data


def resu1(data):
    return None


def resu2(data):
    return None


def test1(resu):
    return False


def test2(resu):
    return False


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
