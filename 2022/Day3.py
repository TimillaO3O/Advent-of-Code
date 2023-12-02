data = open("data.txt").read().splitlines()

sum = [0, 0]
step = 0
for i in range(len(data)):
  step += 1
  lines = [(data[i][:int((len(data[i])/2))]), (data[i][int(len(data[i])/2):])]
  repeat = [True, True]
  for x in data[i-2]:
    if step == 3 and x in data[i-1] and x in data[i] and repeat[0] is True:
      sum[1] += int(ord(x)) - 38 if x.isupper() else int(ord(x)) - 96
      step = 0
      repeat[0] = False
    if x in lines[1] and repeat[1] is True:
      sum[0] += int(ord(x)) - 38 if x.isupper() else int(ord(x)) - 96
      repeat[1] = False
    if repeat[0] is False and repeat[1] is False:
      break
    
print("PART 1: " + str(sum[0]))
print("PART 2: " + str(sum[1]))
