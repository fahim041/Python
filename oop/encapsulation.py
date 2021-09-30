class Computer:
    def __init__(self):
        self.__maxPrice = 900

    def sell(self):
        print("Selling price: {}".format(self.__maxPrice))

    def setMaxPrice(self, price):
        self.__maxPrice = price

c = Computer()
c.sell()
c.setMaxPrice(500)
c.sell()