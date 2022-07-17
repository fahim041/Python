class Product:
    def __init__(self, price) -> None:
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price can not be less  than negative")
        self.__price = value


p = Product(5)
p.price = 10
print(p.price)
