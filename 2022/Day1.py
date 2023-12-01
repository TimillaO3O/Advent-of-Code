data = open("data.txt").read().splitlines()

num = 0
totals = []
for i in data:
  if i.isdigit():
    num += int(i)
  if i == "" or i is data[-1]:
    totals.append(num)
    num = 0
    
totals.sort(reverse=True)

print("PART 1: " + str(totals[0]))
print("PART 2: " + str(totals[0] + totals[1] + totals[2]))
