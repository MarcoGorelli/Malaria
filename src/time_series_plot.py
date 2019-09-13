"""Line plot of malaria deaths over time
"""

import copy
from typing import Any, Dict, List

import pandas as pd

from src import COLOURS, DEATHS


def plot_country_deaths_over_time(code: str) -> pd.DataFrame:
    """Select data (from all years) for given country.
    """
    result: pd.DataFrame = DEATHS.query("Code == '{}'".format(code))[
        ["Year", "Deaths from malaria"]
    ]
    return result


def plotly_line_graph(x_data: List, y_data: List) -> Dict[str, Any]:
    """Return data that can be added to existing plotly graph.
    """
    plotly_data = {
        "hoverlabel": {"namelength": 0},
        "hovertemplate": "Year=%{x}<br>Deaths from malaria=%{y}",
        "legendgroup": "",
        "line": {"color": COLOURS["text"], "dash": "solid"},
        "mode": "lines",
        "name": "",
        "showlegend": False,
        "type": "scatter",
        "x": x_data,
        "xaxis": "x",
        "y": y_data,
        "yaxis": "y",
    }
    return plotly_data


def update_time_series_plot(
    input_value: Dict[str, List], original_map: Dict[str, Any]
) -> Dict[str, Any]:
    """Update time series plot based on user's new click
    """
    code = input_value["points"][0]["location"]

    # Note that this change happens before the deep copy, so it persists.
    if is_same_country(code, original_map):
        original_map["data"][0]["name"] = ""
        return original_map
    original_map["data"][0]["name"] = code  # Keep track of current country.

    data = plot_country_deaths_over_time(code)
    original_map = copy.deepcopy(original_map)
    original_map["data"].append(
        plotly_line_graph(data["Year"], data["Deaths from malaria"])
    )
    return original_map


def is_same_country(code: str, original_map: Dict[str, Any]) -> bool:
    """Check whether user has clicked on same country twice
    """
    if not original_map["data"][0]["name"]:
        return False
    return code == original_map["data"][0]["name"]
