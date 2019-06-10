from algorithm_visualizer import Tracer, _Serializable

class LogTracer(Tracer):
    def set(self, log: _Serializable):
        self.command("set", log)

    def print(self, message: _Serializable):
        self.command("print", message)

    def println(self, message: _Serializable):
        self.command("println", message)

    def printf(self, format: str, *args: _Serializable):
        self.command("printf", format, *args)
