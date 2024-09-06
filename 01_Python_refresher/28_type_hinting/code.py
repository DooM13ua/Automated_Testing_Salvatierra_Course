from typing import List


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


result = list_avg([1, 2, 3])
print(result)


print("----------------------------------")


class Book:
    pass


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."

