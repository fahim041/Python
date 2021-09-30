class Bird:
    species ="Bird"
    def __init__(self, color, age):
        self.color = color
        self.age = age
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("swim faster {}".format(self.age))


class Pengiun(Bird):
    def __init__(self, color, age):
        super().__init__(color, age)

    # override the parent method
    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

    def getColor(self):
        print("color "+self.color)

peggy = Pengiun("white", 20)
peggy.whoisThis()
peggy.swim()
peggy.run()
print(peggy.species)
peggy.run()
peggy.getColor()
