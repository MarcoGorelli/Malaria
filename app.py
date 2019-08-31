import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

from src.visualiser import plot_country_deaths_over_time
from src import DEATHS, COORDS

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

colors = {"background": "#111111", "text": "#7FDBFF"}

app.layout = html.Div(
    style={"backgroundColor": colors["background"]},
    children=[
        html.H1(
            children="Deaths by Malaria",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        html.Div(
            children="""
        In Zambia
    """,
            style={"textAlign": "center", "color": colors["text"]},
        ),
        dcc.Dropdown(
            id="country",
            options=[{"label": i, "value": i} for i in DEATHS.Entity.unique()],
            value="Select country",
        ),
        html.Div(
            className="row",
            children=[
                html.Div(
                    dcc.Graph(
                        figure=px.choropleth(
                            DEATHS.groupby("Code").last().reset_index(),
                            locations="Code",
                            color="Deaths by malaria",
                            hover_name="Entity",  # column to add to hover information
                            color_continuous_scale=px.colors.sequential.Bluered,
                        ).to_dict()
                    ),
                    className="six columns",
                ),
                html.Div(dcc.Graph(id="deaths-by-year"), className="six columns"),
            ],
        ),
    ],
)


@app.callback(
    Output(component_id="deaths-by-year", component_property="figure"),
    [Input(component_id="country", component_property="value")],
)
def update_output_div(input_value="Zambia"):
    return px.line(
        plot_country_deaths_over_time(input_value), x="Year", y="Deaths by malaria"
    ).to_dict()


if __name__ == "__main__":
    app.run_server(debug=True)
