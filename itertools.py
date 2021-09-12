from itertools import count
seq = count(start = 0, step = 2)
while next(seq) <= 10:
  print(next(seq))