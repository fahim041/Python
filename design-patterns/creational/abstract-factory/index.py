class WinButton:
    def print(self):
        print(f"button for windows")


class WinTextInput:
    def print(self):
        print(f"text input for windows")


class MacButton:
    def print(self):
        print(f"button for mac")


class MacTextInput:
    def print(self):
        print(f"text input for mac")


class WinFactory:
    def create_win_button(self):
        return WinButton()

    def create_win_text_input(self):
        return WinTextInput()


class MacFactory:
    def create_mac_button(self):
        return MacButton()

    def create_mac_text_input(self):
        return MacTextInput()


def render(items):
    for item in items:
        item.print()


factory = MacFactory()

m_btn = factory.create_mac_button()
m_input = factory.create_mac_text_input()

render([m_btn, m_input])
