def is_safe(report):
    increase = None
    for j in range(len(report) - 1):
        diff = report[j+1] - report[j]
        if diff == 0 or abs(diff) > 3:
            return False
        if increase is None:
            increase = diff > 0
        elif (diff > 0) != increase:
            return False
    return True


# --- Read the data ---
with open("2024/Data/data2.txt") as f:
    data = [list(map(int, line.split())) for line in f]


# --- Part 1 ---
safe1 = 0
for report in data:
    if is_safe(report):
        safe1 += 1

print("Part 1:", safe1)


# --- Part 2 ---
safe2 = 0
for report in data:
    if is_safe(report):
        safe2 += 1
    else:
        # Try removing one level at a time
        for i in range(len(report)):
            modified = report[:i] + report[i+1:]
            if is_safe(modified):
                safe2 += 1
                break

print("Part 2:", safe2)
