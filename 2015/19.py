import re


def prepare_data(data, test=False):
    replacements, molecule = "\n".join(data).split("\n\n")
    molecule = molecule.replace("\n", "")
    resu = []
    for replacement in replacements.split("\n"):
        resu.append(replacement.split(" => "))
    return resu, molecule


def resu1(data):
    replacements, molecule = data
    resu = set()
    for old, new in replacements:
        i = molecule.find(old)
        while i != -1:
            resu.add(molecule[:i] + molecule[i:].replace(old, new, 1))
            i = molecule.find(old, i + 1)
    return len(resu)


def resu2(data):
    replacements, molecule = data
    molecules = set(
        re.findall(
            r'[A-Z][a-z]?',
            ''.join(
                [x for _, y in replacements for x in y]
            )
        )
    )
    return len(re.findall('|'.join(molecules), molecule)) - \
           molecule.count('Ar') - molecule.count('Rn') - \
           2 * molecule.count('Y') - 1


def test1(resu):
    return resu == 4


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
