def prepare_data(data, test=False):
    root = {"dirs": {}, "files": {}, "parent": None}
    cdir = root
    for line in data:
        line = line.strip()

        if line == "$ cd /":
            cdir = root
            continue
        if line.startswith("$ ls"):
            continue
        if line.startswith("$ cd"):
            _, _, a = line.split(" ")
            if a == "..":
                cdir = cdir["parent"]
                continue
            cdir = cdir["dirs"][a]
            continue
        a, b = line.split(" ")
        if a == "dir":
            cdir["dirs"][b] = {"dirs": {}, "files": {}, "parent": cdir}
            continue
        cdir["files"][b] = int(a)

    comp_size(root)
    return root


def comp_size(cdir):
    size = 0
    for d in cdir["dirs"].values():
        comp_size(d)
        size += d["size"]
    for f in cdir["files"].values():
        size += f
    cdir["size"] = size


def resu1(data):
    resu = sum([resu1(d) for d in data["dirs"].values()])
    if data["size"] < 100000:
        resu += data["size"]
    return resu


def resu2(data, best_rm_size=30_000_000, need_to_remove=None):
    if need_to_remove is None:
        need_to_remove = max(30_000_000 - 70_000_000 + data["size"], 0)

    for _, d in data["dirs"].items():
        best_rm_size = resu2(d, best_rm_size, need_to_remove)

    if best_rm_size > data["size"] > need_to_remove:
        return data["size"]
    return best_rm_size


def test1(resu):
    return resu == 95437


def test2(resu):
    return resu == 24933642


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
