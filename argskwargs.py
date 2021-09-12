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