# def test_var_args(f_args, *args):
#   print("first normal arg: ", f_args)
#   for arg in args:
#     print("another argument: ", arg)

# test_var_args('one', 'two', 'three', 'last')


def test_args_kwargs(uno, dos, tres):
  print("a1: ", uno)
  print("a2: ", dos)
  print("a3: ", tres)

cities = {"uno":"LA", "dos":"ATL", "tres":"Chicago"}
test_args_kwargs(**cities)

subs = {"uno":"Fullerton", "dos":"Suwanee", "tres":"Glenview"}
test_args_kwargs(**subs)

def concatenate(**kwargs):
  str = ''
  for arg in kwargs.values():
    str += arg
  return str

print(concatenate(a='thanks', b='good', c='day', d='.'))

def multiply (*args):
  total = 1
  for arg in args:
    total *= arg
  print ("type: ", type(args))
  return total

print("total: " , multiply(1,3,5))

#destructure
nums = [2, 6, 1]
def summation(*args):
  total = 0
  for num in args:
    total += num
  return total
print("sumOfNums: ", summation(*nums))

def apply (*args, operator):
  if operator == "*":
    return multiply(*args)
  elif operator == "+":
    return summation(*args)
  else:
    return "invalid"

print(apply(*nums, operator="*"))

bob = {"name": "Bob", "age": 25}

def named(**kwargs):
  print(type(kwargs))
  result = ''
  for key, value in kwargs.items():
    result += f' {key}: {value} '
  return result

print(named(**bob))