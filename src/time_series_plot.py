"""Line plot of malaria deaths over time
"""

import copy

import plotly.express as px
import pandas as pd

from src import DEATHS


def plot_country_deaths_over_time(code: str) -> pd.DataFrame:
    """Select data (from all years) for given country.
    """
    return DEATHS.query("Code == '{}'".format(code))[["Year", "Deaths by malaria"]]


def update_time_series_plot(
    input_value: dict, original_map: dict, colours: dict
) -> dict:
    """Update time series plot based on user's new click
    """
    if not input_value:
        return original_map
    if "location" not in input_value["points"][0]:
        return original_map

    code = input_value["points"][0]["location"]
    if is_same_country(code, original_map):
        original_map["data"][0]["name"] = ""
        original_map["data"] = [original_map["data"][0]]
        return original_map

    original_map["data"][0]["name"] = code  # keep track of current country

    time_series = px.line(
        plot_country_deaths_over_time(code), x="Year", y="Deaths by malaria"
    ).to_dict()
    original_map = copy.deepcopy(original_map)
    original_map["data"].append(time_series["data"][0])

    for data in original_map["data"]:
        if "line" in data:
            data["line"]["color"] = colours["text"]
    original_map["layout"]["xaxis"]["title"] = {"text": "Year"}
    original_map["layout"]["yaxis"] = {
        "ticks": "",
        "showgrid": False,
        "showticklabels": False,
    }
    return original_map


def is_same_country(code: str, original_map: dict) -> bool:
    """Check whether user has click on same country twice
    """
    if not original_map["data"][0]["name"]:
        return False
    return code == original_map["data"][0]["name"]
