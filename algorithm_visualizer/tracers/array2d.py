from typing import List

from algorithm_visualizer import Tracer, _Serializable

class Array2DTracer(Tracer):
    def set(self, array2d: List[List[_Serializable]] = None):
        if array2d is None:
            array2d = []
        self.command("set", array2d)

    def patch(self, x: int, y: int, v: _Serializable = None):
        self.command("patch", x, y, v)

    def depatch(self, x: int, y: int):
        self.command("depatch", x, y)

    def select(self, sx: int, sy: int, ex: int = None, ey: int = None):
        if ex is None:
            ex = sx
        if ey is None:
            ey = sy
        self.command("select", sx, sy, ex, ey)

    def selectRow(self, x: int, sy: int, ey: int):
        self.command("selectRow", x, sy, ey)

    def selectCol(self, y: int, sx: int, ex: int):
        self.command("selectCol", y, sx, ex)

    def deselect(self, sx: int, sy: int, ex: int = None, ey: int = None):
        if ex is None:
            ex = sx
        if ey is None:
            ey = sy
        self.command("deselect", sx, sy, ex, ey)

    def deselectRow(self, x: int, sy: int, ey: int):
        self.command("deselectRow", x, sy, ey)

    def deselectCol(self, y: int, sx: int, ex: int):
        self.command("deselectCol", y, sx, ex)
