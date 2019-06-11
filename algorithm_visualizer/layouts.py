from typing import List

from algorithm_visualizer import Commander

class Layout(Commander):
    def __init__(self, children: List[Commander]):
        super().__init__([c.key for c in children])

    @classmethod
    def setRoot(cls, child: Commander):
        cls._command(None, "setRoot", child.key)

    def add(self, child: Commander, index: int = None):
        if index is None:
            self.command("add", child.key)
        else:
            self.command("add", child.key, index)

    def remove(self, child: Commander):
        self.command("remove", child.key)

    def removeAll(self):
        self.command("removeAll")


class HorizontalLayout(Layout):
    pass


class VerticalLayout(Layout):
    pass
