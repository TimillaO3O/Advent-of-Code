data = open("data.txt").read().splitlines()

total = [0, 0]
for i in data:
  lines = [int(i) for i in (i.replace(",", "-")).split("-")]
  if (lines[0] >= lines[2] and lines[1] <= lines[3]) or \
  (lines[2] >= lines[0] and lines[3] <= lines[1]):
    total[0] += 1
  if any(lines[i] >= lines[2] and lines[i] <= lines[3] for i in range(2)) or \
  any(lines[i] >= lines[0] and lines[i] <= lines[1] for i in range(2, 4)):
    total[1] += 1
    
print("PART 1: " + str(total[0]))
print("PART 2: " + str(total[1]))
