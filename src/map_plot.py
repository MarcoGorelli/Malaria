"""Make map so user can select country by clicking on it
"""
from typing import Any, Dict


def make_figure() -> Dict[str, Any]:
    """Make dict that be used to display plotly figure, which captures user clicks
    Most of this was created using:

            world_map = px.choropleth(
                data,
                locations="Code",
                color="Deaths from malaria",
                hover_name="Entity",  # column to add to hover information
                color_continuous_scale=px.colors.sequential.Reds,
            ).to_dict()

    but here I hard-code in the dict for efficiency.
    """

    world_map = {
        "data": [
            {
                "coloraxis": "coloraxis",
                "geo": "geo",
                "hoverlabel": {"namelength": 0},
                "hovertemplate": "<b>%{hovertext}</b><br>Deaths from malaria=%{z}",
                "hovertext": [
                    "Angola",
                    "Burundi",
                    "Benin",
                    "Burkina Faso",
                    "Botswana",
                    "Central African Republic",
                    "Cote d'Ivoire",
                    "Cameroon",
                    "Democratic Republic of Congo",
                    "Congo",
                    "Comoros",
                    "Cape Verde",
                    "Djibouti",
                    "Algeria",
                    "Egypt",
                    "Eritrea",
                    "Ethiopia",
                    "Gabon",
                    "Ghana",
                    "Guinea",
                    "Gambia",
                    "Guinea-Bissau",
                    "Equatorial Guinea",
                    "Kenya",
                    "Liberia",
                    "Libya",
                    "Lesotho",
                    "Morocco",
                    "Madagascar",
                    "Mali",
                    "Mozambique",
                    "Mauritania",
                    "Mauritius",
                    "Malawi",
                    "Namibia",
                    "Niger",
                    "Nigeria",
                    "Rwanda",
                    "Sudan",
                    "Senegal",
                    "Sierra Leone",
                    "Somalia",
                    "South Sudan",
                    "Sao Tome and Principe",
                    "Swaziland",
                    "Seychelles",
                    "Chad",
                    "Togo",
                    "Tunisia",
                    "Tanzania",
                    "Uganda",
                    "South Africa",
                    "Zambia",
                    "Zimbabwe",
                ],
                "locations": [
                    "AGO",
                    "BDI",
                    "BEN",
                    "BFA",
                    "BWA",
                    "CAF",
                    "CIV",
                    "CMR",
                    "COD",
                    "COG",
                    "COM",
                    "CPV",
                    "DJI",
                    "DZA",
                    "EGY",
                    "ERI",
                    "ETH",
                    "GAB",
                    "GHA",
                    "GIN",
                    "GMB",
                    "GNB",
                    "GNQ",
                    "KEN",
                    "LBR",
                    "LBY",
                    "LSO",
                    "MAR",
                    "MDG",
                    "MLI",
                    "MOZ",
                    "MRT",
                    "MUS",
                    "MWI",
                    "NAM",
                    "NER",
                    "NGA",
                    "RWA",
                    "SDN",
                    "SEN",
                    "SLE",
                    "SOM",
                    "SSD",
                    "STP",
                    "SWZ",
                    "SYC",
                    "TCD",
                    "TGO",
                    "TUN",
                    "TZA",
                    "UGA",
                    "ZAF",
                    "ZMB",
                    "ZWE",
                ],
                "name": "",
                "z": [
                    8.43105701e03,
                    8.65867747e03,
                    9.43299055e03,
                    3.05745266e04,
                    5.63766536e00,
                    3.84922576e03,
                    1.62511196e04,
                    2.20405177e04,
                    8.12264767e04,
                    2.24400494e03,
                    1.04496056e00,
                    2.02741853e00,
                    1.74451027e00,
                    6.01598329e00,
                    0.00000000e00,
                    9.58501582e00,
                    2.78352628e03,
                    7.04829651e02,
                    1.87574860e04,
                    1.13554606e04,
                    1.34585709e02,
                    2.34771245e02,
                    9.02358975e02,
                    4.70822437e03,
                    2.81003799e03,
                    0.00000000e00,
                    0.00000000e00,
                    0.00000000e00,
                    5.79911064e03,
                    2.50804711e04,
                    1.84229544e04,
                    2.71102145e02,
                    0.00000000e00,
                    6.88387221e03,
                    8.21068961e00,
                    3.04851391e04,
                    1.52240313e05,
                    3.05231284e03,
                    2.55162602e03,
                    2.14593472e03,
                    1.11186179e04,
                    1.15533381e03,
                    3.86289678e03,
                    4.82682242e-01,
                    5.29540243e00,
                    0.00000000e00,
                    7.67941252e03,
                    6.90431184e03,
                    0.00000000e00,
                    1.53252752e04,
                    2.22367664e04,
                    6.75333069e01,
                    4.67310793e03,
                    6.85682134e02,
                ],
                "type": "choropleth",
            }
        ],
        "layout": {
            "geo": {
                "domain": {"x": [0.0, 0.48], "y": [0.0, 1.0]},
                "center": {},
                "clickmode": "event+select",
                "scope": "africa",
                "bgcolor": "#111111",
                "lakecolor": "aqua",
            },
            "template": {
                "data": {
                    "barpolar": [
                        {
                            "marker": {"line": {"color": "#E5ECF6", "width": 0.5}},
                            "type": "barpolar",
                        }
                    ],
                    "bar": [
                        {
                            "error_x": {"color": "#2a3f5f"},
                            "error_y": {"color": "#2a3f5f"},
                            "marker": {"line": {"color": "#E5ECF6", "width": 0.5}},
                            "type": "bar",
                        }
                    ],
                    "carpet": [
                        {
                            "aaxis": {
                                "endlinecolor": "#2a3f5f",
                                "gridcolor": "white",
                                "linecolor": "white",
                                "minorgridcolor": "white",
                                "startlinecolor": "#2a3f5f",
                            },
                            "baxis": {
                                "endlinecolor": "#2a3f5f",
                                "gridcolor": "white",
                                "linecolor": "white",
                                "minorgridcolor": "white",
                                "startlinecolor": "#2a3f5f",
                            },
                            "type": "carpet",
                        }
                    ],
                    "choropleth": [
                        {
                            "colorbar": {"outlinewidth": 0, "ticks": ""},
                            "type": "choropleth",
                        }
                    ],
                    "contourcarpet": [
                        {
                            "colorbar": {"outlinewidth": 0, "ticks": ""},
                            "type": "contourcarpet",
                        }
                    ],
                    "contour": [
                        {
                            "colorbar": {"outlinewidth": 0, "ticks": ""},
                            "colorscale": [
                                [0.0, "#0d0887"],
                                [0.1111111111111111, "#46039f"],
                                [0.2222222222222222, "#7201a8"],
                                [0.3333333333333333, "#9c179e"],
                                [0.4444444444444444, "#bd3786"],
                                [0.5555555555555556, "#d8576b"],
                                [0.6666666666666666, "#ed7953"],
                                [0.7777777777777778, "#fb9f3a"],
                                [0.8888888888888888, "#fdca26"],
                                [1.0, "#f0f921"],
                            ],
                            "type": "contour",
                        }
                    ],
                    "heatmapgl": [
                        {
                            "colorbar": {"outlinewidth": 0, "ticks": ""},
                            "colorscale": [
                                [0.0, "#0d0887"],
                                [0.1111111111111111, "#46039f"],
                                [0.2222222222222222, "#7201a8"],
                                [0.3333333333333333, "#9c179e"],
                                [0.4444444444444444, "#bd3786"],
                                [0.5555555555555556, "#d8576b"],
                                [0.6666666666666666, "#ed7953"],
                                [0.7777777777777778, "#fb9f3a"],
                                [0.8888888888888888, "#fdca26"],
                                [1.0, "#f0f921"],
                            ],
                            "type": "heatmapgl",
                        }
                    ],
                    "heatmap": [
                        {
                            "colorbar": {"outlinewidth": 0, "ticks": ""},
                            "colorscale": [
                                [0.0, "#0d0887"],
                                [0.1111111111111111, "#46039f"],
                                [0.2222222222222222, "#7201a8"],
                                [0.3333333333333333, "#9c179e"],
                                [0.4444444444444444, "#bd3786"],
                                [0.5555555555555556, "#d8576b"],
                                [0.6666666666666666, "#ed7953"],
                                [0.7777777777777778, "#fb9f3a"],
                                [0.8888888888888888, "#fdca26"],
                                [1.0, "#f0f921"],
                            ],
                            "type": "heatmap",
                        }
                    ],
                    "histogram2dcontour": [
                        {
                            "colorbar": {"outlinewidth": 0, "ticks": ""},
                            "colorscale": [
                                [0.0, "#0d0887"],
                                [0.1111111111111111, "#46039f"],
                                [0.2222222222222222, "#7201a8"],
                                [0.3333333333333333, "#9c179e"],
                                [0.4444444444444444, "#bd3786"],
                                [0.5555555555555556, "#d8576b"],
                                [0.6666666666666666, "#ed7953"],
                                [0.7777777777777778, "#fb9f3a"],
                                [0.8888888888888888, "#fdca26"],
                                [1.0, "#f0f921"],
                            ],
                            "type": "histogram2dcontour",
                        }
                    ],
                    "histogram2d": [
                        {
                            "colorbar": {"outlinewidth": 0, "ticks": ""},
                            "colorscale": [
                                [0.0, "#0d0887"],
                                [0.1111111111111111, "#46039f"],
                                [0.2222222222222222, "#7201a8"],
                                [0.3333333333333333, "#9c179e"],
                                [0.4444444444444444, "#bd3786"],
                                [0.5555555555555556, "#d8576b"],
                                [0.6666666666666666, "#ed7953"],
                                [0.7777777777777778, "#fb9f3a"],
                                [0.8888888888888888, "#fdca26"],
                                [1.0, "#f0f921"],
                            ],
                            "type": "histogram2d",
                        }
                    ],
                    "histogram": [
                        {
                            "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                            "type": "histogram",
                        }
                    ],
                    "mesh3d": [
                        {"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}
                    ],
                    "parcoords": [
                        {
                            "line": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                            "type": "parcoords",
                        }
                    ],
                    "scatter3d": [
                        {
                            "line": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                            "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                            "type": "scatter3d",
                        }
                    ],
                    "scattercarpet": [
                        {
                            "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                            "type": "scattercarpet",
                        }
                    ],
                    "scattergeo": [
                        {
                            "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                            "type": "scattergeo",
                        }
                    ],
                    "scattergl": [
                        {
                            "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                            "type": "scattergl",
                        }
                    ],
                    "scattermapbox": [
                        {
                            "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                            "type": "scattermapbox",
                        }
                    ],
                    "scatterpolargl": [
                        {
                            "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                            "type": "scatterpolargl",
                        }
                    ],
                    "scatterpolar": [
                        {
                            "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                            "type": "scatterpolar",
                        }
                    ],
                    "scatter": [
                        {
                            "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                            "type": "scatter",
                        }
                    ],
                    "scatterternary": [
                        {
                            "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
                            "type": "scatterternary",
                        }
                    ],
                    "surface": [
                        {
                            "colorbar": {"outlinewidth": 0, "ticks": ""},
                            "colorscale": [
                                [0.0, "#0d0887"],
                                [0.1111111111111111, "#46039f"],
                                [0.2222222222222222, "#7201a8"],
                                [0.3333333333333333, "#9c179e"],
                                [0.4444444444444444, "#bd3786"],
                                [0.5555555555555556, "#d8576b"],
                                [0.6666666666666666, "#ed7953"],
                                [0.7777777777777778, "#fb9f3a"],
                                [0.8888888888888888, "#fdca26"],
                                [1.0, "#f0f921"],
                            ],
                            "type": "surface",
                        }
                    ],
                    "table": [
                        {
                            "cells": {
                                "fill": {"color": "#EBF0F8"},
                                "line": {"color": "white"},
                            },
                            "header": {
                                "fill": {"color": "#C8D4E3"},
                                "line": {"color": "white"},
                            },
                            "type": "table",
                        }
                    ],
                },
                "layout": {
                    "annotationdefaults": {
                        "arrowcolor": "#2a3f5f",
                        "arrowhead": 0,
                        "arrowwidth": 1,
                    },
                    "colorscale": {
                        "diverging": [
                            [0, "#8e0152"],
                            [0.1, "#c51b7d"],
                            [0.2, "#de77ae"],
                            [0.3, "#f1b6da"],
                            [0.4, "#fde0ef"],
                            [0.5, "#f7f7f7"],
                            [0.6, "#e6f5d0"],
                            [0.7, "#b8e186"],
                            [0.8, "#7fbc41"],
                            [0.9, "#4d9221"],
                            [1, "#276419"],
                        ],
                        "sequential": [
                            [0.0, "#0d0887"],
                            [0.1111111111111111, "#46039f"],
                            [0.2222222222222222, "#7201a8"],
                            [0.3333333333333333, "#9c179e"],
                            [0.4444444444444444, "#bd3786"],
                            [0.5555555555555556, "#d8576b"],
                            [0.6666666666666666, "#ed7953"],
                            [0.7777777777777778, "#fb9f3a"],
                            [0.8888888888888888, "#fdca26"],
                            [1.0, "#f0f921"],
                        ],
                        "sequentialminus": [
                            [0.0, "#0d0887"],
                            [0.1111111111111111, "#46039f"],
                            [0.2222222222222222, "#7201a8"],
                            [0.3333333333333333, "#9c179e"],
                            [0.4444444444444444, "#bd3786"],
                            [0.5555555555555556, "#d8576b"],
                            [0.6666666666666666, "#ed7953"],
                            [0.7777777777777778, "#fb9f3a"],
                            [0.8888888888888888, "#fdca26"],
                            [1.0, "#f0f921"],
                        ],
                    },
                    "colorway": [
                        "#636efa",
                        "#EF553B",
                        "#00cc96",
                        "#ab63fa",
                        "#FFA15A",
                        "#19d3f3",
                        "#FF6692",
                        "#B6E880",
                        "#FF97FF",
                        "#FECB52",
                    ],
                    "font": {"color": "#7FDBFF"},
                    "geo": {
                        "bgcolor": "#111111",
                        "lakecolor": "white",
                        "landcolor": "#E5ECF6",
                        "showlakes": True,
                        "showland": True,
                        "subunitcolor": "white",
                    },
                    "hoverlabel": {"align": "left"},
                    "hovermode": "closest",
                    "mapbox": {"style": "light"},
                    "paper_bgcolor": "#111111",
                    "plot_bgcolor": "#E5ECF6",
                    "polar": {
                        "angularaxis": {
                            "gridcolor": "white",
                            "linecolor": "white",
                            "ticks": "",
                        },
                        "bgcolor": "#E5ECF6",
                        "radialaxis": {
                            "gridcolor": "white",
                            "linecolor": "white",
                            "ticks": "",
                        },
                    },
                    "scene": {
                        "xaxis": {
                            "backgroundcolor": "#E5ECF6",
                            "gridcolor": "white",
                            "gridwidth": 2,
                            "linecolor": "white",
                            "showbackground": True,
                            "ticks": "",
                            "zerolinecolor": "white",
                        },
                        "yaxis": {
                            "backgroundcolor": "#E5ECF6",
                            "gridcolor": "white",
                            "gridwidth": 2,
                            "linecolor": "white",
                            "showbackground": True,
                            "ticks": "",
                            "zerolinecolor": "white",
                        },
                        "zaxis": {
                            "backgroundcolor": "#E5ECF6",
                            "gridcolor": "white",
                            "gridwidth": 2,
                            "linecolor": "white",
                            "showbackground": True,
                            "ticks": "",
                            "zerolinecolor": "white",
                        },
                    },
                    "shapedefaults": {"line": {"color": "#2a3f5f"}},
                    "ternary": {
                        "aaxis": {
                            "gridcolor": "white",
                            "linecolor": "white",
                            "ticks": "",
                        },
                        "baxis": {
                            "gridcolor": "white",
                            "linecolor": "white",
                            "ticks": "",
                        },
                        "bgcolor": "#E5ECF6",
                        "caxis": {
                            "gridcolor": "white",
                            "linecolor": "white",
                            "ticks": "",
                        },
                    },
                    "title": {"x": 0.05},
                    "xaxis": {
                        "automargin": True,
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": "",
                        "zerolinecolor": "white",
                        "zerolinewidth": 2,
                    },
                    "yaxis": {
                        "automargin": True,
                        "gridcolor": "white",
                        "linecolor": "white",
                        "ticks": "",
                        "zerolinecolor": "white",
                        "zerolinewidth": 2,
                    },
                },
            },
            "coloraxis": {
                "colorscale": [
                    [0.0, "rgb(255,245,240)"],
                    [0.125, "rgb(254,224,210)"],
                    [0.25, "rgb(252,187,161)"],
                    [0.375, "rgb(252,146,114)"],
                    [0.5, "rgb(251,106,74)"],
                    [0.625, "rgb(239,59,44)"],
                    [0.75, "rgb(203,24,29)"],
                    [0.875, "rgb(165,15,21)"],
                    [1.0, "rgb(103,0,13)"],
                ],
                "colorbar": {
                    "title": {"text": "Deaths from malaria in 2017", "side": "bottom"},
                    "x": 0,
                },
            },
            "legend": {"tracegroupgap": 0},
            "margin": {"t": 60},
            "height": 600,
            "paper_bgcolor": "#111111",
            "xaxis": {
                "domain": [0.52, 0.98],
                "showgrid": False,
                "title": {"text": "Year"},
            },
            "yaxis": {"showgrid": False, "showticklabels": False, "ticks": ""},
            "plot_bgcolor": "#111111",
        },
    }

    return world_map
