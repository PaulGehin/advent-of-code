import re


def prepare_data(data, test=False):
    resu, i = [{}], 0
    for line in data:
        if line == "" or line == "\n":
            resu.append({})
            i += 1
        else:
            for unit in line.split(" "):
                key, value = unit.strip("\n").split(":")
                resu[i][key] = value
    return resu


def valid(passport):
    try:
        byr = 1920 <= int(passport["byr"]) <= 2002
        iyr = 2010 <= int(passport["iyr"]) <= 2020
        eyr = 2020 <= int(passport["eyr"]) <= 2030
        hgt = float(passport["hgt"][:-2])
        hgtunit = passport["hgt"][-2:]
        hgt = hgtunit == "cm" and 150 <= hgt <= 193 or hgtunit == "in" and 59 <= hgt <= 76
        hcl = len(re.findall("^#[0-9a-f]{6}$", passport["hcl"])) == 1
        ecl = passport["ecl"] in ["amb", "blu",
                                  "brn", "gry", "grn", "hzl", "oth"]
        pid = len(re.findall("^[0-9]{9}$", passport["pid"])) == 1
        return byr and iyr and eyr and hgt and hcl and ecl and pid
    except Exception:
        return False


def resu1(data):
    def valid(passport):
        for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if not key in passport.keys():
                return False
        return True

    return list(map(valid, data)).count(True)


def resu2(data):
    def valid(passport):
        try:
            byr = 1920 <= int(passport["byr"]) <= 2002
            iyr = 2010 <= int(passport["iyr"]) <= 2020
            eyr = 2020 <= int(passport["eyr"]) <= 2030
            hgt = float(passport["hgt"][:-2])
            hgtunit = passport["hgt"][-2:]
            hgt = hgtunit == "cm" and 150 <= hgt <= 193 or hgtunit == "in" and 59 <= hgt <= 76
            hcl = len(re.findall("^#[0-9a-f]{6}$", passport["hcl"])) == 1
            ecl = passport["ecl"] in ["amb", "blu",
                                      "brn", "gry", "grn", "hzl", "oth"]
            pid = len(re.findall("^[0-9]{9}$", passport["pid"])) == 1
            return byr and iyr and eyr and hgt and hcl and ecl and pid
        except Exception:
            return False

    return list(map(valid, data)).count(True)


def test1(resu):
    return resu == 2


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
