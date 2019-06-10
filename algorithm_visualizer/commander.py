import string
from typing import Any, Dict, List

from algorithm_visualizer import randomize

_MAX_COMMANDS = 1000000
_MAX_OBJECTS = 100


class Commander:
    _keyRandomizer = randomize.String(8, string.ascii_lowercase + string.digits)
    _objectCount = 0
    commands: List[Dict[str, Any]] = []

    def __init__(self, *args):
        self._objectCount += 1
        self.command(self.__class__.__name__, *args)

    @classmethod
    def command(cls, method: str, *args, key: str = _keyRandomizer.create()):
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

    @classmethod
    def destroy(cls):
        cls._objectCount -= 1
        cls.command("destroy")
