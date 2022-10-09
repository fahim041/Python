class EditorState:
    def __init__(self, content: str) -> None:
        self.__content = content

    def get_content(self):
        return self.__content


class Editor:
    def __init__(self) -> None:
        self.__content = ""

    def set_content(self, value: str) -> str:
        self.__content = value

    def create_state(self) -> EditorState:
        return EditorState(self.__content)

    def restore(self, state: EditorState) -> None:
        self.__content = state.get_content()

    def __str__(self) -> str:
        return str(f"content --> {self.__content}")


class History:
    def __init__(self) -> None:
        self.__states = []

    def save(self, state: EditorState):
        self.__states.append(state)

    def undo(self):
        return self.__states.pop()


editor = Editor()
history = History()

editor.set_content('a')
history.save(editor.create_state())

editor.set_content('b')
history.save(editor.create_state())

editor.set_content('c')
editor.restore(history.undo())

print(editor)
