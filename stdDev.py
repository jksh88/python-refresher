import math

numFrq = {10: 1, 12: 1, 16: 2, 21: 1, 23: 3}

print(numFrq[10] + numFrq[12])
print(list(numFrq)[2]*numFrq[16])

sum = 0
avg = 0
count = 0

for key in numFrq:
  sum += key*numFrq[key]
  count += numFrq[key]
  avg = sum/count

sumOfSqr = 0
for key in numFrq:
  sumOfSqr += (key - avg)**2*numFrq[key] 

std = math.sqrt(sumOfSqr / (count - 1))

print(sumOfSqr)
print("avg: " + str(avg))
print("sd: " + str(std))



