class Animal:
    def __init__(self) -> None:
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self) -> None:
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
m.eat()
print(m.age)
