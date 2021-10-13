class Person:
  def __init__ (self, name, language):
    self.name = name
    self.language = language

  def __str__ (self):
    return f'{self.name}: {self.language}'

  def __repr__ (self):
    return f"{self.name}, {self.language[0]}"

bobby = Person ("Bobby", ("Python", "Javascript"))
print(bobby)

# print(bobby.__repr__)

