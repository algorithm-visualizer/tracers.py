from typing import List

from . import chart
from .array2d import Array2DTracer
from algorithm_visualizer.types import Serializable


class Array1DTracer(Array2DTracer):
    def set(self, array1d: List[Serializable] = None):
        super().set(array1d)

    def patch(self, x: int, v: Serializable = None):
        self.command("patch", x, v)

    def depatch(self, x: int):
        self.command("depatch", x)

    def select(self, sx: int, ex: int = None):
        super().select(0, sx, 0, ex)

    def deselect(self, sx: int, ex: int = None):
        super().deselect(0, sx, 0, ex)

    def chart(self, chartTracer: "chart.ChartTracer"):
        self.command("chart", chartTracer.key)
