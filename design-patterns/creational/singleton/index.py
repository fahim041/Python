class Application:
    instance = None

    def __init__(self) -> None:
        self.logged = False

    @staticmethod
    def getAppState():
        if not Application.instance:
            Application.instance = Application()
        return Application.instance


state1 = Application.getAppState()
print(state1.logged)

state2 = Application.getAppState()
state2.logged = True

print(state1.logged)
print(Application.instance)
print(state1)
print(state2)
