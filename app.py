"""Web app showing African map and deaths by malaria over time for
country user clicks on
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from src import DEATHS
from src.time_series_plot import update_time_series_plot
from src.map_plot import make_figure

EXTERNAL_STYLESHEETS = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
APP = dash.Dash("Malaria")
APP.css.append_css({"external_url": "./static/reset.css"})
APP.css.config.serve_locally = False
APP.server.static_folder = "static"
SERVER = APP.server
COLOURS = {"background": "#111111", "text": "#7FDBFF"}

# maybe, here we can have a map of just Africa with no line graph as a constant
# and then, have another function which determines how to update the other part
# of that plot
WORLD_MAP = make_figure(
    DEATHS.query("Continent_Code == 'AF'").groupby("Code").last().reset_index(), COLOURS
)

APP.layout = html.Div(
    style={"backgroundColor": COLOURS["background"]},
    children=[
        html.H1(
            children="Deaths by Malaria",
            style={"textAlign": "center", "color": COLOURS["text"]},
        ),
        html.Div(
            id="country_text", style={"textAlign": "center", "color": COLOURS["text"]}
        ),
        html.Div(id="plots", children=[dcc.Graph(id="plotly", figure=WORLD_MAP)]),
    ],
)


@APP.callback(
    Output(component_id="plotly", component_property="figure"),
    [Input(component_id="plotly", component_property="clickData")],
)
def update_output_div(input_value):
    """Update times series plot based on country from country map which
    user clicks on
    """
    print(input_value)
    return update_time_series_plot(input_value, WORLD_MAP, COLOURS)


# @APP.callback(
#     Output(component_id="country_text", component_property="children"),
#     [Input(component_id="g2", component_property="clickData")],
# )
# def update_text(input_value):
#     """Update text to reflect what's shown in the time series
#     """
#     if not input_value:
#         country = "Zambia"
#     else:
#         country = input_value["points"][0]["hovertext"]
#     return f"In {country}"


if __name__ == "__main__":
    APP.run_server(debug=False)
