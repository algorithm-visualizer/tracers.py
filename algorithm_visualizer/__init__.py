import atexit
import json
import os
from typing import Union

from algorithm_visualizer import randomize as Randomize
from algorithm_visualizer.commander import Commander
from algorithm_visualizer.tracers import *

__all__ = (
    "Randomize", "Commander",
    "Array1DTracer", "Array2DTracer", "ChartTracer", "GraphTracer", "LogTracer", "Tracer"
)

# Types which are serializable by the default JSONEncoder
_Serializable = Union[dict, list, str, int, float, bool, None]
_Number = Union[int, float]


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
