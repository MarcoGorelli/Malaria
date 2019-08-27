import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

from src.visualiser import plot_country_deaths_over_time
from src import DATA

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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
            options=[{"label": i, "value": i} for i in DATA.Entity.unique()],
            value="Select country",
        ),
        dcc.Graph(id="deaths-by-year"),
    ],
)


@app.callback(
    Output(component_id="deaths-by-year", component_property="figure"),
    [Input(component_id="country", component_property="value")],
)
def update_output_div(input_value):
    return px.line(
        plot_country_deaths_over_time(input_value), x="Year", y="Deaths by malaria"
    ).to_dict()


if __name__ == "__main__":
    app.run_server(debug=True)
