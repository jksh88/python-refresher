items = [2,5,6,10]
squared = lambda x:x**2
squaredList = list(map(squared, items))
print(squaredList)

def multiply(x, y):
  return x*y

def add(x,y):
  return x+y

funcs = [multiply, add]
listOfTuples = [(2,3),(4,5),(6,7)]
for i in listOfTuples:
  print(list(map(lambda a: a(i[0], i[1]), funcs)))

numList = range(-3,3)
negative = list(filter(lambda a: a < 0, numList))
print(negative)

from functools import reduce
product = reduce((lambda x, y: x * y), [2,3,4])
print(product)