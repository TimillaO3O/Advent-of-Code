data = open("data.txt").read().splitlines()

dict = {
    "A": {"X": [4, 3], "Y": [8, 4], "Z": [3, 8]},
    "B": {"X": [1, 1], "Y": [5, 5], "Z": [9, 9]},
    "C": {"X": [7, 2], "Y": [2, 6], "Z": [6, 7]}
}
points = [0, 0]
for i in data:
  result = dict[i[0]].get(i[2])
  if result is not None:
    points[0] += result[0]
    points[1] += result[1]

print("PART 1: " + str(points[0]))
print("PART 2: " + str(points[1]))
