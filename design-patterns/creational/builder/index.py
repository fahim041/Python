class Button:
    def __init__(self, os) -> None:
        self.os = os
        self.width = None
        self.height = None

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def __str__(self) -> str:
        return f'os: {self.os}, height: {self.height}, width: {self.width}'


class ButtonBuilder:
    def __init__(self, os) -> None:
        self.button = Button(os)

    def Width(self, width):
        self.button.setWidth(width)
        return self

    def Height(self, height):
        self.button.setHeight(height)
        return self

    def build(self):
        return self.button


w_btn = ButtonBuilder('windows').Height(100).Width(50).build()
print(w_btn)
