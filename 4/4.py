import re

with open("scrathcards.txt", "r") as f:
    res = []
    copias = [1]*203
    total = 203

    for i, line in enumerate(f.readlines()):
        points = 0
        ocu = 0

        winners = re.findall(r"(\d+)", "".join(line[10:].split("|")[0]))
        numbers = re.findall(r"(\d+)", "".join(line[10:].split("|")[1]))

        for w in winners:
            if w in numbers:
                # Part 1
                if points == 0: points = 1
                else:           points *= 2
                # Part 2
                ocu += 1
        res.append(points)

        for k in range(copias[i]):
            for j in range(ocu):
                copias[i+j+1] += 1

        total += copias[i]*ocu

    print("Parte 1:", sum(res))
    print("Parte 2:", total)
