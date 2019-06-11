import atexit
import json
import os

from . import randomize as Randomize
from .commander import Commander
from .layouts import *
from .tracers import *

__all__ = (
    "Randomize", "Commander",
    "Array1DTracer", "Array2DTracer", "ChartTracer", "GraphTracer", "LogTracer", "Tracer",
    "HorizontalLayout", "Layout", "VerticalLayout"
)


@atexit.register
def execute():
    if os.getenv("ALGORITHM_VISUALIZER"):
        with open("visualization.json", "w", encoding="UTF-8") as file:
            json.dump(Commander.commands, file)
    else:
        import requests
        import webbrowser

        response = requests.post(
            "https://algorithm-visualizer.org/api/visualizations",
            json=Commander.commands
        )

        if response.status_code == 200:
            webbrowser.open(response.text)
        else:
            raise requests.HTTPError(response=response)
