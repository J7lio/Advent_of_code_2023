import re

maxs=[12, 13, 14]

with open("bags.txt", "r") as f:
    res = []
    for line in f.readlines():
        n_game = re.search(r"(\d+)", line)[1]
        valid = True

        for i in range(line.count(";")+1):
            part = line.split("; ")[i]
            n_red = re.search(r"(\d+) red", part)
            if n_red:
                n_red = n_red[1]
            else:
                n_red = 0
            n_green = re.search(r"(\d+) green", part)
            if n_green:
                n_green = n_green[1]
            else:
                n_green = 0
            n_blue = re.search(r"(\d+) blue", part)
            if n_blue:
                n_blue = n_blue[1]
            else:
                n_blue = 0

            for n, limit in zip([n_red, n_green, n_blue], maxs):
                if int(n) > limit:
                    valid = False

        if valid:
            res.append(int(n_game))

    print(sum(res))

