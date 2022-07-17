from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print('Textbox')


class DropDownList(UIControl):
    def draw(self):
        print('Drop down')


def draw(control):
    control.draw()


t = TextBox()
draw(t)
