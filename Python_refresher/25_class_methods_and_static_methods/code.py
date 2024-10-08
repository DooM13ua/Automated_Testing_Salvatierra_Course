class ClassTest:
    def instance_method(self):
        print(f'Called instance_method of {self}')

    @classmethod
    def class_method(cls):
        print(f'Called class_method of {cls}')

    @staticmethod
    def static_method():
        print(f'Called static_method.')


test = ClassTest()
test.instance_method()
ClassTest.class_method()
ClassTest.static_method()


print('----------------------------------------------')


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f'<Book {self.name}, {self.book_type}, weighing {self.weight}g.>'

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name:str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)


book = Book.hardcover('Harry Potter', 1500)
light = Book.paperback('Python 101', 600)

print(book)
print(light)