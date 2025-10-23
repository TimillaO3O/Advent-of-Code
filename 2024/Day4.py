with open("2024/Data/data4.txt") as f:
    data = [list(line.strip()) for line in f]

found = 0
for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        if data[i][j] == "X":
            # Check Down
            if i <= len(data) - 4 and data[i + 1][j] == "M" and data[i + 2][j] == "A" and data[i + 3][j] == "S":
                found += 1
            # Check Left
            if j >= 3 and data[i][j-1] == "M" and data[i][j-2] == "A" and data[i][j-3] == "S":
                found += 1
            # Check Right
            if j <= len(data[i]) - 4 and data[i][j+1] == "M" and data[i][j+2] == "A" and data[i][j+3] == "S":
                found += 1
            # Check Up
            if i >= 3 and data[i - 1][j] == "M" and data[i - 2][j] == "A" and data[i - 3][j] == "S":
                found += 1
            # Check Down Left
            if i <= len(data) - 4 and j >= 3 and data[i + 1][j-1] == "M" and data[i + 2][j-2] == "A" and data[i + 3][j-3] == "S":
                found += 1
            # Check Down Right
            if i <= len(data) - 4 and j <= len(data[i]) - 4 and data[i + 1][j+1] == "M" and data[i + 2][j+2] == "A" and data[i + 3][j+3] == "S":
                found += 1
            # Check Up Left
            if i >= 3 and j >= 3 and data[i - 1][j-1] == "M" and data[i - 2][j-2] == "A" and data[i - 3][j-3] == "S":
                found += 1
            # Check Up Right
            if i >= 3 and j <= len(data[i]) - 4 and data[i - 1][j+1] == "M" and data[i - 2][j+2] == "A" and data[i - 3][j+3] == "S":
                found += 1

print("Part 1:", found)

found = 0

for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):
        if data[i][j] == "A":
            # Check the two diagonals that cross the A
            # Diagonal 1: top-left to bottom-right
            diag1 = [data[i - 1][j - 1], data[i][j], data[i + 1][j + 1]]
            # Diagonal 2: top-right to bottom-left
            diag2 = [data[i - 1][j + 1], data[i][j], data[i + 1][j - 1]]

            # Each diagonal must spell MAS or SAM
            if (diag1 in (["M", "A", "S"], ["S", "A", "M"]) and
                diag2 in (["M", "A", "S"], ["S", "A", "M"])):
                found += 1

print("Part 2:", found)