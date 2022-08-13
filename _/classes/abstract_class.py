from abc import ABC, abstractmethod


class InvalidOperation(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperation("already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperation("already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print('reading file data')


class NetworkStream(Stream):
    def read(self):
        print('reading network data')
