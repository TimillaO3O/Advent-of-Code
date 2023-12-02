data = open("data.txt").read().splitlines()

numbers = [0,0]
for i in data:
  strings = ["", ""]
  for x in range(len(i)):
    if i[x].isdigit():
      strings[0] += i[x]
      strings[1] += i[x]
    for j, y in enumerate(["zero", "one", "two", 
    "three", "four", "five", 
    "six", "seven", "eight", "nine"]):
      if i[x:].startswith(y):
        strings[1] += str(j)
  numbers[0] += int((strings[0])[0] + (strings[0])[-1])
  numbers[1] += int((strings[1])[0] + (strings[1])[-1])

print("PART 1: " + str(numbers[0]))
print("PART 2: " + str(numbers[1]))
