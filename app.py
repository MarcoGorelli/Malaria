"""Web app showing African map and deaths by malaria over time for
country user clicks on
"""

import argparse
from typing import Any, Dict, List

import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

from src import COLOURS, DEATHS
from src.map_plot import make_figure
from src.time_series_plot import update_time_series_plot

EXTERNAL_STYLESHEETS = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
APP = dash.Dash("Malaria")
APP.css.append_css({"external_url": "./static/reset.css"})
APP.css.config.serve_locally = False
APP.server.static_folder = "static"
SERVER: flask.app.Flask = APP.server

WORLD_MAP: Dict[str, Any] = make_figure(
    DEATHS.query("Continent_Code == 'AF'").groupby("Code").last().reset_index(), COLOURS
)

APP.layout = html.Div(
    style={"backgroundColor": COLOURS["background"]},
    children=[
        html.H1(
            children="Deaths from Malaria",
            style={"textAlign": "center", "color": COLOURS["text"]},
        ),
        html.H2(
            id="Country text", style={"textAlign": "center", "color": COLOURS["text"]}
        ),
        html.Div(
            id="plots",
            children=[
                dcc.Graph(
                    id="plotly", figure=WORLD_MAP, config={"displayModeBar": False}
                )
            ],
        ),
        html.A(
            "Source code",
            href="https://github.com/MarcoGorelli/Malaria",
            target="_blank",
            style={"textAlign": "center", "color": COLOURS["text"]},
        ),
    ],
)


@APP.callback(
    Output(component_id="plotly", component_property="figure"),
    [Input(component_id="plotly", component_property="clickData")],
)
def update_output_div(input_value: Dict[str, List]) -> Dict[str, Any]:
    """Update times series plot based on country from country map which
    user clicks on
    """
    print(input_value)
    if not input_value:
        raise PreventUpdate()
    if "location" not in input_value["points"][0]:
        raise PreventUpdate()
    new_plot: Dict[str, Any] = update_time_series_plot(input_value, WORLD_MAP)
    from pprint import pprint

    pprint(new_plot)
    return new_plot


@APP.callback(
    Output(component_id="Country text", component_property="children"),
    [Input(component_id="plotly", component_property="clickData")],
)
def update_text(input_value: Dict[str, List]) -> str:
    """Update text to reflect what's shown in the time series
    """
    if not input_value:
        return "Click on a country!"
    if "location" not in input_value["points"][0]:
        raise PreventUpdate()
    country: str = input_value["points"][0]["hovertext"]
    return country


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="Should the app run in debug mode?")
    PARSER.add_argument(
        "--debug",
        type=bool,
        help="Pass False to not run in debug mode",
        required=False,
        default=False,
    )
    ARGS: argparse.Namespace = PARSER.parse_args()
    APP.run_server(debug=ARGS.debug)
