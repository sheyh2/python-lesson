# 1
class MyClass:
    def __init__(self, name) -> None:
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        self.items.append({
                "name": name,
                "price": price
            })
    
    def stock_price(self):
        total = 0
        # for product in self.items:
        #     total += product["price"]
        
        return sum([item["price"] for item in self.items])

myClass = MyClass("Product")
myClass.add_item("apple", 15)
myClass.add_item("banana", 35)

print(myClass.stock_price())
# myClass.stock_price() 