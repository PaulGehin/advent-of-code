import math
import os
import sys
import time
from datetime import date

import requests
from bs4 import BeautifulSoup

import credentials


def get_today() -> int: return int(date.today().strftime("%d"))


def get_month() -> int: return int(date.today().strftime("%m"))


def get_year() -> int: return int(date.today().strftime("%Y"))


def format_day(day: int | str) -> str: return str(day).zfill(2)


def format_runtime(sec: float) -> str:
    ms = sec * 1000
    if ms <= 1:
        return f"{round(ms * 1000)}µs"
    elif ms < 1000:
        whole_ms = math.floor(ms)
        rem_ms = ms - whole_ms
        return f"{whole_ms}ms {format_runtime(rem_ms / 1000)}"
    elif sec < 60:
        whole_sec = math.floor(sec)
        rem_sec = sec - whole_sec
        return f"{whole_sec}s {format_runtime(rem_sec)}"
    else:
        return f"{round(sec // 60)}m {format_runtime(sec % 60)}"


def get_data(day: int, year: int, code, test: bool = False):
    folder_name = f"{year}/{'test' if test else 'data'}"
    filename = f"{folder_name}/{format_day(day)}.txt"
    start = time.perf_counter()

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    if not test and not os.path.exists(filename):
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        r = requests.get(url, cookies=credentials.cookies())
        with open(filename, 'wb') as file:
            file.write(r.content)

    with open(filename, "r") as file:
        data = file.read().splitlines()

    f = getattr(code, "prepare_data", None)
    if callable(f):
        data = f(data, test)

    end = time.perf_counter()
    runtime = end - start

    if not test:
        print(f"Runtime {format_runtime(runtime)}")
    return data


def verify_test(part, code, resu):
    f = getattr(code, f"test{part}", None)
    if callable(f):
        return f(resu)
    else:
        return False


def already_submitted(day: int, year: int, part: int) -> bool:
    r = requests.get(url=f"https://adventofcode.com/{year}", cookies=credentials.cookies())
    soup = BeautifulSoup(r.content, 'html.parser')
    line = soup.find("a", class_=f"calendar-day{day}")
    complete = "calendar-complete" in line["class"]
    very_complete = "calendar-verycomplete" in line["class"]
    return part == 1 and complete or very_complete


def submit_data(day: int, year: int, part: int, resu: str) -> bool:
    if already_submitted(day, year, part):
        return True
    print(f"Try to submit ({year}/{day} => {resu})")
    r = requests.post(url=f"https://adventofcode.com/{year}/day/{day}/answer",
                      data={
                          "level": f"{part}",
                          "answer": f"{resu}"
                      },
                      cookies=credentials.cookies())
    return "That's the right answer!" in r.text


def check_data(day: int, year: int, part: int, resu: str) -> bool:
    r = requests.get(url=f"https://adventofcode.com/{year}/day/{day}", cookies=credentials.cookies())
    soup = BeautifulSoup(r.content, 'html.parser')
    code = soup.select(f"body > main > p > code")
    return str(resu) == code[part-1].text


def run_part(part, code, data, test=False, day=None, year=None, submit=False, check=False):
    f = getattr(code, f"resu{part}", None)
    if callable(f):
        start = time.perf_counter()
        resu = f(data)
        end = time.perf_counter()
        runtime = end - start
        if test:
            return verify_test(part, code, resu)
        if resu is not None:
            print(f"Output: {resu}")
            if submit and day is not None and year is not None:
                print(f"Completed: {submit_data(day, year, part, resu)}")
            if check:
                print(f"Check: {check_data(day, year, part, resu)}")
        print(f"Runtime {format_runtime(runtime)}")


def run_year(year=get_year(), bypasstest=False, check=False):
    if year == get_year() and (get_month() < 12 or get_today() < 25):
        year -= 1
    for day in range(1, 26):
        try:
            run(day=day, year=year, bypasstest=bypasstest, check=check)
        finally:
            ...


def run(day=get_today(), year=get_year(), bypasstest=False, submit=True, check=False):
    start = time.perf_counter()
    print(f"Date: {format_day(day)}/12/{year}")
    code = getattr(__import__(f"{year}.{format_day(day)}"), format_day(day))

    print(f"Load dataset")
    if not bypasstest:
        datatest = get_data(day, year, code, test=True)
    data = get_data(day, year, code)

    for part in range(1, 3):
        print(f"Part {part}")
        if bypasstest or run_part(part, code, data=datatest, test=True):
            run_part(part, code, data=data, test=False, day=day, year=year, submit=submit, check=check)
        else:
            print("Test Failed")

    end = time.perf_counter()
    runtime = end - start
    print(f"Total runtime: {format_runtime(runtime)}", end="\n\n")


def run_file(abspath: str | bytes, bypasstest: bool = False, submit: bool = True):
    day = int(os.path.splitext(os.path.basename(abspath))[0])
    year = int(os.path.basename(os.path.dirname(abspath)))
    sys.path.append(os.path.dirname(os.path.dirname(abspath)))
    run(day=day, year=year, bypasstest=bypasstest, submit=submit)
