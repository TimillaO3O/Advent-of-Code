import re

data = open("2024/Data/data3.txt").read()

matches = re.findall(r"mul\((\d+),(\d+)\)", data)

results = [(int(a), int(b)) for a, b in matches]
products = [a * b for a, b in results]

print("Part 1 :", sum(products))

pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"

tokens = re.findall(pattern, data)

enabled = True  # mul() starts enabled
total = 0

for token in tokens:
    if token == "do()":
        enabled = True
    elif token == "don't()":
        enabled = False
    elif token.startswith("mul") and enabled:
        a, b = map(int, re.findall(r"\d+", token))
        total += a * b

print("Part 2:", total)