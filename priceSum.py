class Store:
  def __init__(self, name):
    self.name = name
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

  # @classmethod
  # def franchise(self):
    # return f"{self.name} - franchise"
  
  @classmethod
  def franchise(cls, name):
    return f"{Store.store_details(name)} - franchise"

  @staticmethod
  def store_details(store):
    return Store.__str__(store)
  
target = Store("Target")
amazon = Store("Amazon")
# target.add_item('bananas', 8)
# target.add_item('shoes', 30)
# total = target.stock_price()
# print(total)
print(target.franchise("Target"))
print(target)
print(Store.store_details("Target"))