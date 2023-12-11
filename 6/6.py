import re

with open("races.txt", "r") as f:
    file = f.read().split("\n")
    times = [int(x) for x in re.findall(r"\d+", file[0])]
    records = [int(x) for x in re.findall(r"\d+", file[1])]

    res = 1
    for t, r in zip(times, records):
        count = 0
        for i in range(t+1):
            if (i*(t-i)) > r:
                count += 1
        res *= count
    print(res)
