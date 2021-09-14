# def hi(name='J'):
#   def greet():
#     return "in greet function"
#   def welcome():
#     return "in welcome function"
#   if name == 'J':
#     return greet
#   else:
#     return welcome

# a = hi('O')

# print(hi()())


def new_decorator(func):
  def wrapTheFunc():
    print("before func")
    func()
    print("after executing func")
  return wrapTheFunc

def func_requiring_decoration():
  print("inside func_requiring_decoration")

func_requiring_decoration()
func_requiring_decoration = new_decorator(func_requiring_decoration)
func_requiring_decoration()
