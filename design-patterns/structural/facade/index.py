class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.__arr = [0] * 2

    def append(self, val):
        if self.length == self.capacity:
            self.resize()
        self.__arr[self.length] = val
        self.length += 1

    def pop(self):
        if self.length > 0:
            self.__arr.pop(self.length - 1)
            self.length -= 1

    def resize(self):
        self.capacity = 2 * self.capacity
        newArray = [0] * self.capacity

        for i in range(self.length):
            newArray[i] = self.__arr[i]

        self.__arr = newArray

    def __iter__(self):
        self.head = 0
        return self

    def __next__(self):
        val = self.__arr[self.head]
        self.head += 1
        if val:
            return val
        else:
            raise StopIteration


a = Array()

a.append(1)
a.append(2)
a.append(3)

a.pop()

for i in a:
    print(i)
