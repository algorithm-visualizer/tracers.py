from typing import List, Optional

from .log import LogTracer, Tracer
from algorithm_visualizer.types import Number, Serializable


class GraphTracer(Tracer):
    def set(self, array2d: List[List[Serializable]] = None):
        if array2d is None:
            array2d = []
        self.command("set", array2d)

    def directed(self, isDirected: bool = True):
        self.command("directed", isDirected)

    def weighted(self, isWeighted: bool = True):
        self.command("weighted", isWeighted)
        return self

    def layoutCircle(self):
        self.command("layoutCircle")
        return self

    def layoutTree(self, root: Any = 0, sorted: bool = False):
        self.command("layoutTree", root, sorted)
        return self

    def layoutRandom(self):
        self.command("layoutRandom")
        return self

    def addNode(
        self,
        id: Serializable,
        weight: Optional[Number] = None,
        x: int = 0,
        y: int = 0,
        visitedCount: int = 0,
        selectedCount: int = 0
    ):
        self.command("addNode", id, weight, x, y, visitedCount, selectedCount)

    def updateNode(
        self,
        id: Serializable,
        weight: Optional[Number] = None,
        x: int = 0,
        y: int = 0,
        visitedCount: int = 0,
        selectedCount: int = 0
    ):
        self.command("updateNode", id, weight, x, y, visitedCount, selectedCount)

    def removeNode(self, id: Serializable):
        self.command("removeNode", id)

    def addEdge(
        self,
        source: Serializable,
        target: Serializable,
        weight: Optional[Number] = None,
        visitedCount: int = 0,
        selectedCount: int = 0
    ):
        self.command("addEdge", source, target, weight, visitedCount, selectedCount)

    def updateEdge(
        self,
        source: Serializable,
        target: Serializable,
        weight: Optional[Number] = None,
        visitedCount: int = 0,
        selectedCount: int = 0
    ):
        self.command("updateEdge", source, target, weight, visitedCount, selectedCount)

    def removeEdge(self, source: Serializable, target: Serializable):
        self.command("removeEdge", source, target)

    def visit(
        self,
        target: Serializable,
        source: Serializable = None,
        weight: Optional[Number] = None
    ):
        self.command("visit", target, source, weight)

    def leave(
        self,
        target: Serializable,
        source: Serializable = None,
        weight: Optional[Number] = None
    ):
        self.command("leave", target, source, weight)

    def select(self, target: Serializable, source: Serializable = None):
        self.command("select", target, source)

    def deselect(self, target: Serializable, source: Serializable = None):
        self.command("deselect", target, source)

    def log(self, log: LogTracer):
        self.command("log", log.key)
