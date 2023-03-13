from abc import ABC, abstractmethod


class FilterStretegy(ABC):
    @abstractmethod
    def removeValue(self, val):
        pass


class RemoveNegativeStrategy(FilterStretegy):
    def removeValue(self, val):
        return val < 0


class RemoveOddStrategy(FilterStretegy):
    def removeValue(self, val):
        return abs(val) % 2


class Values:
    def __init__(self, vals):
        self.vals = vals

    def filter(self, strategy):
        res = []
        for n in self.vals:
            if not strategy.removeValue(n):
                res.append(n)
        return res


values = Values([3, 6, 1, -4, 6, -3])

print(values.filter(RemoveNegativeStrategy()))
print(values.filter(RemoveOddStrategy()))
