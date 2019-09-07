"""Make map so user can select country by clicking on it
"""

import plotly.express as px


def make_figure(data, colours):
    """Make dict that be used to display plotly figure, which captures user clicks
    """
    world_map = px.choropleth(
        data,
        locations="Code",
        color="Deaths by malaria",
        hover_name="Entity",  # column to add to hover information
        color_continuous_scale=px.colors.sequential.Reds,
    ).to_dict()
    world_map["layout"].update({"clickmode": "event+select"})
    world_map["layout"]["geo"]["scope"] = "africa"
    world_map["layout"]["geo"]["bgcolor"] = colours["background"]
    world_map["layout"]["geo"]["lakecolor"] = "aqua"
    world_map["layout"]["paper_bgcolor"] = colours["background"]
    world_map["layout"]["template"]["layout"]["font"]["color"] = colours["text"]
    return world_map
