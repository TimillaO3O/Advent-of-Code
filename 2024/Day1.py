data = open("2024/Data/data1.txt").read().split()

leftSide = []
rightSide = []
for i in range(0, len(data), 2):
    leftSide.append(data[i])
    rightSide.append(data[i+1])

leftSide.sort()
rightSide.sort()

sum = 0
for i in range(0, len(leftSide)):
    sum += abs(int(leftSide[i]) - int(rightSide[i]))

print("Part 1: %d", sum)

simScore = 0
for i in leftSide:
    simScore += int(i) * rightSide.count(i)

print("Part 2: %d", simScore)