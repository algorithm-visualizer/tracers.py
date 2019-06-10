from algorithm_visualizer import Commander


class Tracer(Commander):
    def __init__(self, title: str = None):
        if title is None:
            super().__init__()
        else:
            super().__init__(title)

    @classmethod
    def delay(cls, lineNumber: int = None):
        if lineNumber is None:
            cls._command(None, "delay")
        else:
            cls._command(None, "delay", lineNumber)

    def set(self):
        self.command("set")

    def reset(self):
        self.command("reset")
