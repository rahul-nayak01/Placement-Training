# wrire a py pgm to create a cart representing shopping cart.Include methods for adding and removing items and calculating total price.
"""
class Cart(object):
    def __init__(self,items,price):
        self.items=items
        self.price=price
    def add(self,items,price):
        self.items.append(items)
        self.price=self.price+price

    def remove(self,items,price):
        self.items.remove(items)
        self.price=self.price-price

    def calculate(self,price):
"""
#0r
"""
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append({'item': item, 'price': price})

    def remove_item(self, item):
        for i, cart_item in enumerate(self.items):
            if cart_item['item'] == item:
                del self.items[i]
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

# Example usage:
cart = Cart()
cart.add_item('Apple', 1.00)
cart.add_item('Banana', 0.50)
print(cart.calculate_total())  
cart.remove_item('Apple')
print(cart.calculate_total())  

"""

