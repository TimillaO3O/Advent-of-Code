data = open("data.txt").read().splitlines()

total = [0, 0]
color_indices = {"blue": 0, "red": 1, "green": 2}
for i in data:
  lines = i.split(" ")
  least = [0, 0, 0]
  good = True
  for x in range(len(lines)):
    if "blue" in lines[x] and int(lines[x-1]) > 14 or \
    "red" in lines[x] and int(lines[x-1]) > 12 or \
    "green" in lines[x] and int(lines[x-1]) > 13:
        good = False
    for color in color_indices:
      index = color_indices[color]
      if color in lines[x] and int(lines[x-1]) > least[index]:
          least[index] = int(lines[x-1])
  if good is True:
    total[0] += int((lines[1])[:-1])
  total[1] += least[0] * least[1] * least[2]
  
print("PART 1: " + str(total[0]))
print("PART 2: " + str(total[1]))
