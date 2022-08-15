# 1
# class ClassTest:
#     def instance_meyhod(self):
#         print(f"Called instance_method of {self}")
    
#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls}")
    
#     @staticmethod
#     def statick_method():
#         print("Called statick_method.")



# ClassTest.instance_meyhod()
# ClassTest.class_method()
# ClassTest.statick_method()

# 2
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight) -> None:
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book.hardcover("Harry Poter", 1500)
light = Book.paperback("Python 101", 600)

print(book)
print(light)