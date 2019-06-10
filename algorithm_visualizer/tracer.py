from algorithm_visualizer import Commander


class Tracer(Commander):
    def __init__(self, title: str = None):
        if title is None:
            super().__init__()
        else:
            super().__init__(title)

    @classmethod
    def delay(cls, lineNumber: int = None):
        cls.command("delay", lineNumber)

    @classmethod
    def set(cls):
        cls.command("set")

    @classmethod
    def reset(cls):
        cls.command("reset")
