from abc import ABC, abstractmethod


class Tool(ABC):
    @abstractmethod
    def mouseDown(self) -> None:
        pass

    @abstractmethod
    def mouseUp(self) -> None:
        pass


class SelectionTool(Tool):
    def mouseDown(self) -> None:
        print("Selection icon")

    def mouseUp(self) -> None:
        print("Draw a dashed rectangle")


class BrushTool(Tool):
    def mouseDown(self) -> None:
        print("Brush icon")

    def mouseUp(self) -> None:
        print("Draw a line")


class Canvas:
    def __init__(self) -> None:
        self.__current_tool = None

    def set_current_tool(self, tool: Tool) -> None:
        self.__current_tool = tool

    def mouseDown(self) -> None:
        self.__current_tool.mouseDown()

    def mouseUp(self) -> None:
        self.__current_tool.mouseUp()


canvas = Canvas()
canvas.set_current_tool(SelectionTool())
canvas.mouseDown()
canvas.mouseUp()
canvas.set_current_tool(BrushTool())
canvas.mouseDown()
canvas.mouseUp()
