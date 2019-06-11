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
    commands = json.dumps(Commander.commands, separators=(",", ":"))
    if os.getenv("ALGORITHM_VISUALIZER"):
        with open("visualization.json", "w", encoding="UTF-8") as file:
            file.write(commands)
    else:
        import requests
        import webbrowser

        response = requests.post(
            "https://algorithm-visualizer.org/api/visualizations",
            headers={"Content-type": "application/json"},
            data=commands
        )

        if response.status_code == 200:
            webbrowser.open(response.text)
        else:
            raise requests.HTTPError(response=response)
