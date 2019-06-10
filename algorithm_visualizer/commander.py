import string
from typing import Any, Dict, List, Optional

from algorithm_visualizer import Randomize, _Serializable

_MAX_COMMANDS = 1000000
_MAX_OBJECTS = 100


class Commander:
    _keyRandomizer = Randomize.String(8, string.ascii_lowercase + string.digits)
    _objectCount = 0
    commands: List[Dict[str, Any]] = []

    def __init__(self, *args):
        self._objectCount += 1
        self.key = self._keyRandomizer.create()
        self.command(self.__class__.__name__, *args)

    @classmethod
    def _command(cls, key: Optional[str], method: str, *args: _Serializable):
        cmd = {
            "key": key,
            "method": method,
            "args": args
        }
        cls.commands.append(cmd)

        if len(cls.commands) > _MAX_COMMANDS:
            raise RuntimeError("Too Many Commands")
        elif cls._objectCount > _MAX_OBJECTS:
            raise RuntimeError("Too Many Objects")

    def command(self, method: str, *args):
        self._command(self.key, method, *args)

    def destroy(self):
        self._objectCount -= 1
        self.command("destroy")
