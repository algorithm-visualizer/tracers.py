import string
from typing import Any, Dict, List

from algorithm_visualizer import randomize

_MAX_COMMANDS = 1000000
_MAX_OBJECTS = 100


class Commander:
    _keyRandomizer = randomize.String(8, string.ascii_lowercase + string.digits)
    _objectCount = 0
    commands: List[Dict[str, Any]] = []

    def __init__(self, **kwargs):
        self._objectCount += 1
        self.command(self.__class__.__name__, **kwargs)

    @classmethod
    def command(cls, method: str, key: str = _keyRandomizer.create(), **kwargs):
        cmd = {
            "key": key,
            "method": method
        }
        cmd.update(kwargs)
        cls.commands.append(cmd)

        if len(cls.commands) > _MAX_COMMANDS:
            raise RuntimeError("Too Many Commands")
        elif cls._objectCount > _MAX_OBJECTS:
            raise RuntimeError("Too Many Objects")

    @classmethod
    def destroy(cls):
        cls._objectCount -= 1
        cls.command("destroy")
