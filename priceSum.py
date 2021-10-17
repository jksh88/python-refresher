class Store:
  def __init__(self, name):
    self.name = name
    self.items = []

  def add_item(self, name, price):
    self.items.append({self.name: self.price})

  def stock_price(self):
    total = 0
    for price in self.items[self.name]:
      total += price
    return price

  
grocery = Store("Target")
grocery.add_item('bananas', 8)
grocery.add_item('shoes', 30)