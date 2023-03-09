class Button:
    def __init__(self, os):
        self.os = os

    def print(self):
        print(f"button for {self.os}")


class ButtonFactory:
    def windows_button(self):
        return Button('windows')

    def mac_button(self):
        return Button('mac')

    def linux_button(self):
        return Button('linux')


factory = ButtonFactory()

w_btn = factory.windows_button()
m_btn = factory.mac_button()

w_btn.print()
m_btn.print()
