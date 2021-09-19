def dedupe(array):
  lst = []
  for x in array:
    if x in lst:
      continue
    else:
      lst.append(x)
  return lst

print(dedupe([1,2,2,2,4]))
print(dedupe([33,44,50,49]))
print(list(dict.fromkeys([1,2,2,2,4])))