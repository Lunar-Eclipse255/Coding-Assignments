fileList = open("Python/Mini Projects/AC Day 3 Rucksack Reorganization.txt").read().strip().split("\n")


def getVal(x):
    return ord(x) - ord('a') + 1 if x.islower() else ord(x) - ord('A') + 27

rucksackOne = 0
for line in fileList:
    m = len(line) // 2
    x, = set(line[:m]) & set(line[m:])
    rucksackOne += getVal(x)

rucksackTwo=0
for i in range(0, len(fileList), 3):
    line1, line2, line3 = fileList[i:i+3]
    x, = set(line1) & set(line2) & set(line3)
    rucksackTwo += getVal(x)
print("Part1", rucksackOne)
print("Part2", rucksackTwo)
