class Store:
  def __init__(self):
    # self.name = name
    self.items = []

  def add_item(self, name, price):
    # self.name = name
    # self.price = price
    self.items.append({'name': name, 'price': price})

  def stock_price(self):
    total = 0
    for item in self.items:
      total += item['price']
    return total

  
grocery = Store()
grocery.add_item('bananas', 8)
grocery.add_item('shoes', 30)
total = grocery.stock_price()
print(total)