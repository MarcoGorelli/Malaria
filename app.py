import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

from src.visualiser import plot_country_deaths_over_time
from src import DEATHS

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

COLORS = {"background": "#111111", "text": "#7FDBFF"}

WORLD_MAP = px.choropleth(
    DEATHS.query("Continent_Code == 'AF'").groupby("Code").last().reset_index(),
    locations="Code",
    color="Deaths by malaria",
    hover_name="Entity",  # column to add to hover information
    color_continuous_scale=px.colors.sequential.Reds,
).to_dict()
WORLD_MAP["layout"].update({"clickmode": "event+select"})
WORLD_MAP["layout"]["geo"]["scope"] = "africa"
WORLD_MAP["layout"]["geo"]["bgcolor"] = COLORS["background"]
WORLD_MAP["layout"]["geo"]["lakecolor"] = "aqua"
WORLD_MAP["layout"]["paper_bgcolor"] = COLORS["background"]
WORLD_MAP["layout"]["template"]["layout"]["font"]["color"] = COLORS["text"]

app.layout = html.Div(
    style={"backgroundColor": COLORS["background"]},
    children=[
        html.H1(
            children="Deaths by Malaria",
            style={"textAlign": "center", "color": COLORS["text"]},
        ),
        html.Div(
            id="country_text", style={"textAlign": "center", "color": COLORS["text"]}
        ),
        html.Div(
            className="row",
            children=[
                html.Div(
                    dcc.Graph(id="country", figure=WORLD_MAP), className="six columns"
                ),
                html.Div(dcc.Graph(id="deaths-by-year"), className="six columns"),
            ],
        ),
    ],
)


@app.callback(
    Output(component_id="deaths-by-year", component_property="figure"),
    [Input(component_id="country", component_property="clickData")],
)
def update_output_div(input_value):
    if not input_value:
        country = "Zambia"
    else:
        country = input_value["points"][0]["hovertext"]
    OVER_TIME_MAP = px.line(
        plot_country_deaths_over_time(country), x="Year", y="Deaths by malaria"
    ).to_dict()
    OVER_TIME_MAP["layout"]["template"]["layout"]["geo"]["bgcolor"] = COLORS[
        "background"
    ]
    OVER_TIME_MAP["layout"]["template"]["layout"]["paper_bgcolor"] = COLORS[
        "background"
    ]
    OVER_TIME_MAP["layout"]["template"]["layout"]["font"]["color"] = COLORS["text"]
    OVER_TIME_MAP["layout"]["xaxis"]["showgrid"] = False
    OVER_TIME_MAP["layout"]["yaxis"]["showgrid"] = False
    OVER_TIME_MAP["layout"]["plot_bgcolor"] = COLORS["background"]
    for data in OVER_TIME_MAP["data"]:
        data["line"]["color"] = COLORS["text"]
    OVER_TIME_MAP["layout"]["xaxis"]["title"]["text"] = ""
    OVER_TIME_MAP["layout"]["yaxis"]["title"]["text"] = ""
    return OVER_TIME_MAP


@app.callback(
    Output(component_id="country_text", component_property="children"),
    [Input(component_id="country", component_property="clickData")],
)
def update_text(input_value):
    if not input_value:
        country = "Zambia"
    else:
        country = input_value["points"][0]["hovertext"]
    return f"In {country}"


if __name__ == "__main__":
    app.run_server(debug=True)
