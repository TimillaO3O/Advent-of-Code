data = open("data.txt").read().splitlines()

part1 = 0
part2 = 0
for i in data:
  p1 = ""
  p2 = ""
  for x in range(len(i)):
    if i[x].isdigit():
      p1 += i[x]
      p2 += i[x]
    for j, y in enumerate(["zero", "one", "two", 
    "three", "four", "five", 
    "six", "seven", "eight", "nine"]):
      if i[x:].startswith(y):
        p2 += str(j)
  part1 += int(p1[0] + p1[-1])
  part2 += int(p2[0] + p2[-1])

print("PART 1: " + str(part1))
print("PART 2: " + str(part2))
