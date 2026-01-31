class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
#__iter__ method to make the class return an iterable object
    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}
r = Rectangle(10, 5)
#same output as below using __iter__ method
# print({"length": r.length},"\n" , {"width": r.width})
for i in r:
    print(i)
