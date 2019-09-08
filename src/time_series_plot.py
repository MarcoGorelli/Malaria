"""Line plot of malaria deaths over time
"""

import copy

import plotly.express as px

from src import DEATHS


def plot_country_deaths_over_time(code):
    """Select data (from all years) for given country.
    """
    return DEATHS.query("Code == '{}'".format(code))[["Year", "Deaths by malaria"]]


def update_time_series_plot(input_value, original_map, colours):
    """Update time series plot based on user's new click
    """
    if not input_value:
        return original_map
    if not "location" in input_value["points"][0]:
        return original_map

    code = input_value["points"][0]["location"]
    time_series = (
        px.line(plot_country_deaths_over_time(code), x="Year", y="Deaths by malaria")
        .update_yaxes(showticklabels=False)
        .to_dict()
    )
    original_map = copy.deepcopy(original_map)
    original_map["data"].append(time_series["data"][0])
    original_map["layout"]["xaxis"] = {"domain": [0.52, 0.98]}
    original_map["layout"]["yaxis"] = {}
    original_map["layout"]["template"]["layout"]["geo"]["bgcolor"] = colours[
        "background"
    ]
    original_map["layout"]["template"]["layout"]["paper_bgcolor"] = colours[
        "background"
    ]
    original_map["layout"]["template"]["layout"]["font"]["color"] = colours["text"]
    original_map["layout"]["xaxis"]["showgrid"] = False
    original_map["layout"]["yaxis"]["showgrid"] = False
    original_map["layout"]["plot_bgcolor"] = colours["background"]
    for data in original_map["data"]:
        if "line" in data:
            data["line"]["color"] = colours["text"]
    # original_map["layout"]["xaxis"]["title"] = {"text": ""}
    # original_map["layout"]["yaxis"]["title"]["text"] = ""
    return original_map
