import re

with open("calibration.txt", "r") as f:
    res = []
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numsinv = ["orez", "eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]
    for line in f.readlines():
        num1 = re.search(r"\d|zero|one|two|three|four|five|six|seven|eight|nine", line)[0]
        if num1 in nums:
            num1 = str(nums.index(num1))
        num2 = re.search(r"\d|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno|orez", line[::-1])[0]
        if num2 in numsinv:
            num2 = str(numsinv.index(num2))
        res.append(int(num1+num2))
    print(sum(res))