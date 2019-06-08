from tracer import Commander


class Tracer(Commander):
    def __init__(self, title: str = None):
        super().__init__(title=title or {})

    @classmethod
    def delay(cls, lineNumber: int = None):
        cls.command("delay", lineNumber=lineNumber or {})

    @classmethod
    def set(cls):
        cls.command("set")

    @classmethod
    def reset(cls):
        cls.command("reset")
