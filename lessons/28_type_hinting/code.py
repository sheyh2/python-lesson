# 1
# from typing import List

# def list_avg(sequence: list) -> float:
#     return sum(sequence) / len(sequence)

# list_avg(123)

# 2
# class Book:
#     def __init__(self, name: str,  page_count: int) -> None:
#         self.name = name
#         self.page_count = page_count

# 3
# from typing import List

# class Book:
#     def __init__(self, name) -> None:
#         self.name = name

#     def __str__(self) -> str:
#         return f"Book {self.name}"


# class BookShelf:
#     def __init__(self, books: List[Book]) -> None:
#         self.books = books
    
#     def __str__(self) -> str:
#         return f"BookShelf with {len(self.books)} books."

# 4
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighting {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)