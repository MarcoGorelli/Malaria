"""Make map so user can select country by clicking on it
"""
from typing import Any, Dict

import pandas as pd
import plotly.express as px

from src import TIME_SERIES


def make_figure(data: pd.DataFrame, colours: Dict[str, str]) -> Dict[str, Any]:
    """Make dict that be used to display plotly figure, which captures user clicks
    """
    world_map = px.choropleth(
        data,
        locations="Code",
        color="Deaths from malaria",
        hover_name="Entity",  # column to add to hover information
        color_continuous_scale=px.colors.sequential.Reds,
    ).to_dict()
    world_map["layout"]["geo"]["domain"]["x"] = [0.0, 0.48]
    world_map["data"][0][
        "hovertemplate"
    ] = "<b>%{hovertext}</b><br>Deaths from malaria=%{z}"
    world_map["layout"]["coloraxis"]["colorbar"]["x"] = 0
    world_map["layout"]["coloraxis"]["colorbar"]["title"][
        "text"
    ] = "Deaths from malaria in 2017"
    world_map["layout"]["coloraxis"]["colorbar"]["title"]["side"] = "bottom"
    world_map["layout"]["geo"]["clickmode"] = "event+select"
    world_map["layout"]["geo"]["scope"] = "africa"
    world_map["layout"]["geo"]["bgcolor"] = colours["background"]
    world_map["layout"]["geo"]["lakecolor"] = "aqua"
    world_map["layout"]["paper_bgcolor"] = colours["background"]
    world_map["layout"]["template"]["layout"]["font"]["color"] = colours["text"]
    world_map["layout"]["xaxis"] = {"domain": [0.52, 0.98]}
    world_map["layout"]["yaxis"] = {}
    world_map["layout"]["template"]["layout"]["geo"]["bgcolor"] = colours["background"]
    world_map["layout"]["template"]["layout"]["paper_bgcolor"] = colours["background"]
    world_map["layout"]["template"]["layout"]["font"]["color"] = colours["text"]
    world_map["layout"]["xaxis"]["showgrid"] = False
    world_map["layout"]["yaxis"]["showgrid"] = False
    world_map["layout"]["plot_bgcolor"] = colours["background"]
    world_map["layout"].update(TIME_SERIES["layout"])

    return world_map
