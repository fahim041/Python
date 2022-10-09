from typing import List, Any
from abc import ABC, abstractmethod


class Iterator:
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def next(self):
        pass


class BrowserHistory:
    def __init__(self) -> None:
        self.__collection: List[Any] = []

    def push(self, url: str) -> None:
        self.__collection.append(url)

    def pop(self) -> str:
        return self.__collection.pop()

    def get_urls(self):
        return self.__collection

    def get_current_index(self, index):
        return self.__collection[index]

    def create_iterator(self):
        return ListIterator(self)


class ListIterator(Iterator):
    def __init__(self, history: BrowserHistory) -> None:
        self.__history = history
        self.__index = 0

    def has_next(self) -> bool:
        return self.__index < len(self.__history.get_urls())

    def current(self):
        return self.__history.get_current_index(self.__index)

    def next(self):
        self.__index += 1


history = BrowserHistory()
history.push("a")
history.push("b")
history.push("c")

iterator = history.create_iterator()
while iterator.has_next():
    print(iterator.current())
    iterator.next()
