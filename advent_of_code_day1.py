# Advent of Code 2021 Day 1

with open("./data/input-day1.txt") as f:
    depths = []

    for line in f:
        depths.append(int(line))

print(depths)

increase = 0
for i in range(len(depths)):
    # print(depths[i])
    if depths[1] > depths[0]:
        increase += 1
    else:
        increase + 0
    if depths[2] > depths[1]:
        increase += 1
    else:
        increase + 0
    if depths[3] > depths[2]:
        increase += 1
    else:
        increase + 0
    if depths[4] > depths[3]:
        increase += 1
    else:
        increase + 0
    if depths[5] > depths[4]:
        increase += 1
    else:
        increase += 0
    if depths[6] > depths[5]:
        increase += 1
    else:
        increase + 0
    if depths[7] > depths[6]:
        increase += 1
    else:
        increase + 0
    if depths[8] > depths[7]:
        increase += 1
    else:
        increase += 0
    if depths[9] > depths[8]:
        increase += 1
    else:
        increase + 0

print(f"There are {increase / 10} measurements larger than the previous measurement")