class Series(object):
  def __init__(self, low, high):
    self.current = low
    self.high = high
  
  def __iter__(self):
    return self

  def __next__(self):
    if self.current > self.high:
      raise StopIteration
    else:
      self.current += 1
      return self.current - 1

n_list = Series(1, 10)
print(type(n_list))
print(n_list)
print(list(n_list))