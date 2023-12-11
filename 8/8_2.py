import re
import math

with open("directions.txt") as f:
    dirs = f.readline().strip().replace("R", "1").replace("L", "0")
    mapa = {}

    for line in f.readlines():
        mapa[line[0:3]] = (line[7:10], line[12:15])

    way = re.findall(r"\w\wA", " ".join(mapa))
    c = 0
    steps = 0

    count = 0

    # Terriblemente ineficiente nsq del mcm ni idea
    while len(re.findall(r"\w\wZ", " ".join(way))) != len(way):

        for i, w in enumerate(way):
            way[i] = mapa[w][int(dirs[c])]

        c += 1
        steps += 1
        if c >= len(dirs):
            c = 0

        print(steps)
