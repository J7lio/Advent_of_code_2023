with open("directions.txt") as f:
    dirs = f.readline().strip().replace("R", "1").replace("L", "0")
    print(len(dirs))
    mapa = {}

    for line in f.readlines():
        mapa[line[0:3]] = (line[7:10], line[12:15])

    way = "AAA"
    c = 0
    steps = 0

    while way != "ZZZ":
        way = mapa[way][int(dirs[c])]
        c += 1
        steps += 1
        if c >= len(dirs):
            c = 0

    print(steps)