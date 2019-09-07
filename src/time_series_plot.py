"""Line plot of malaria deaths over time
"""

import plotly.express as px

from src import DEATHS


def plot_country_deaths_over_time(country):
    """Select data (from all years) for given country.
    """
    return DEATHS.query("Entity == '{}'".format(country))[["Year", "Deaths by malaria"]]


def update_time_series_plot(input_value, colours):
    """Update time series plot based on user's new click
    """
    if not input_value:
        country = "Zambia"
    else:
        country = input_value["points"][0]["hovertext"]
    time_series = px.line(
        plot_country_deaths_over_time(country), x="Year", y="Deaths by malaria"
    ).to_dict()
    time_series["layout"]["template"]["layout"]["geo"]["bgcolor"] = colours[
        "background"
    ]
    time_series["layout"]["template"]["layout"]["paper_bgcolor"] = colours["background"]
    time_series["layout"]["template"]["layout"]["font"]["color"] = colours["text"]
    time_series["layout"]["xaxis"]["showgrid"] = False
    time_series["layout"]["yaxis"]["showgrid"] = False
    time_series["layout"]["plot_bgcolor"] = colours["background"]
    for data in time_series["data"]:
        data["line"]["color"] = colours["text"]
    time_series["layout"]["xaxis"]["title"]["text"] = ""
    time_series["layout"]["yaxis"]["title"]["text"] = ""
    return time_series
