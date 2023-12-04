import re
import math

with open("bags.txt", "r") as f:
    res = []
    for line in f.readlines():
        actual_maxs = [0, 0, 0]
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

            for j, (n, color_max) in enumerate(zip([n_red, n_green, n_blue], actual_maxs)):
                if int(n) > color_max:
                    actual_maxs[j] = int(n)

        res.append(math.prod(actual_maxs))

    print(sum(res))
