class Animal:
    name = "Animal"

    def eat(self):
        print("eat")


class Mammal(Animal):
    # name = "Mammal"
    def walk(self):
        print("walk")


m = Mammal()
m.walk()
m.eat()

print(m.name)
