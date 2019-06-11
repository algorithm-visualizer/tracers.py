from typing import List

import algorithm_visualizer
from algorithm_visualizer import Array2DTracer, _Serializable

class Array1DTracer(Array2DTracer):
    def set(self, array1d: List[_Serializable] = None):
        super().set(array1d)

    def patch(self, x: int, v: _Serializable = None):
        self.command("patch", x, v)

    def depatch(self, x: int):
        self.command("depatch", x)

    def select(self, sx: int, ex: int = None):
        super().select(0, sx, 0, ex)

    def deselect(self, sx: int, ex: int = None):
        super().deselect(0, sx, 0, ex)

    def chart(self, chartTracer: "algorithm_visualizer.ChartTracer"):
        self.command("chart", chartTracer.key)
