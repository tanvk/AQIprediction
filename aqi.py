import plotly.graph_objects as go
from os import link
import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, title="Breathe2", update_title='Loading...')

df = pd.read_csv("sample.csv")
dff = df.copy()

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='MIT', children=[
            dcc.Graph(
                figure= go.Figure(
                    go.Indicator(
                        mode="gauge+number+delta",
                        value = 153,
                        domain= {"x": [0,1], "y":[0,1]},
                        title= {"text": "MIT", "font": {"size": 24}},
                        gauge={
                            "axis": {
                                "range": [None, 500],
                                "tickwidth": 1,
                                "tickcolor": "black",
                                "tickmode": "linear",
                                "dtick": 50,
                            },
                        "bar": {"color": "lightgrey"},
                        "bgcolor": "white",
                        "borderwidth": 2,
                        "bordercolor": "gray",
                        "steps": [
                            {"range": [0, 50], "color": "green"},
                            {
                                "range": [50, 100],
                                "color": "yellow",
                            },
                            {
                                "range": [100, 150],
                                "color": "orange",
                            },
                            {
                                "range": [150, 200],
                                "color": "red",
                            },
                            {
                                "range": [200, 300],
                                "color": "blue",
                            },
                            {
                                "range": [300, 500],
                                "color": "#620042",
                            },
                        ],
                        "threshold": {
                            "line": {"color": "black", "width": 4},
                            "thickness": 0.75,
                            "value": 150,
                        },
                        }
                    )
                )
            )
        ]),
        dcc.Tab(label='IMD', children=[
            dcc.Graph(
                figure=go.Figure(
                    go.Indicator(
                        mode="gauge+number+delta",
                        value = 89,
                        domain= {"x": [0,1], "y":[0,1]},
                        title= {"text": "IMD", "font": {"size": 24}},
                        gauge={
                            "axis": {
                                "range": [None, 500],
                                "tickwidth": 1,
                                "tickcolor": "black",
                                "tickmode": "linear",
                                "dtick": 50,
                            },
                        "bar": {"color": "lightgrey"},
                        "bgcolor": "white",
                        "borderwidth": 2,
                        "bordercolor": "gray",
                        "steps": [
                            {"range": [0, 50], "color": "green"},
                            {
                                "range": [50, 100],
                                "color": "yellow",
                            },
                            {
                                "range": [100, 150],
                                "color": "orange",
                            },
                            {
                                "range": [150, 200],
                                "color": "red",
                            },
                            {
                                "range": [200, 300],
                                "color": "blue",
                            },
                            {
                                "range": [300, 500],
                                "color": "#620042",
                            },
                        ],
                        "threshold": {
                            "line": {"color": "black", "width": 4},
                            "thickness": 0.75,
                            "value": 150,
                        },
                        }
                    )
                )
            )
        ]),
        dcc.Tab(label='Indira Hall', children=[
            dcc.Graph(
                figure=go.Figure(
                    go.Indicator(
                        mode="gauge+number+delta",
                        value = 189,
                        domain= {"x": [0,1], "y":[0,1]},
                        title= {"text": "Indira Hall", "font": {"size": 24}},
                        gauge={
                            "axis": {
                                "range": [None, 500],
                                "tickwidth": 1,
                                "tickcolor": "black",
                                "tickmode": "linear",
                                "dtick": 50,
                            },
                        "bar": {"color": "lightgrey"},
                        "bgcolor": "white",
                        "borderwidth": 2,
                        "bordercolor": "gray",
                        "steps": [
                            {"range": [0, 50], "color": "green"},
                            {
                                "range": [50, 100],
                                "color": "yellow",
                            },
                            {
                                "range": [100, 150],
                                "color": "orange",
                            },
                            {
                                "range": [150, 200],
                                "color": "red",
                            },
                            {
                                "range": [200, 300],
                                "color": "blue",
                            },
                            {
                                "range": [300, 500],
                                "color": "#620042",
                            },
                        ],
                        "threshold": {
                            "line": {"color": "black", "width": 4},
                            "thickness": 0.75,
                            "value": 150,
                        },
                        }
                    )
                )
            )
        ]),
        dcc.Tab(label='Bapat Hospital', children=[
            dcc.Graph(
                figure=go.Figure(
                    go.Indicator(
                        mode="gauge+number+delta",
                        value = 42,
                        domain= {"x": [0,1], "y":[0,1]},
                        title= {"text": "Bapat Hospital", "font": {"size": 24}},
                        gauge={
                            "axis": {
                                "range": [None, 500],
                                "tickwidth": 1,
                                "tickcolor": "black",
                                "tickmode": "linear",
                                "dtick": 50,
                            },
                        "bar": {"color": "lightgrey"},
                        "bgcolor": "white",
                        "borderwidth": 2,
                        "bordercolor": "gray",
                        "steps": [
                            {"range": [0, 50], "color": "green"},
                            {
                                "range": [50, 100],
                                "color": "yellow",
                            },
                            {
                                "range": [100, 150],
                                "color": "orange",
                            },
                            {
                                "range": [150, 200],
                                "color": "red",
                            },
                            {
                                "range": [200, 300],
                                "color": "blue",
                            },
                            {
                                "range": [300, 500],
                                "color": "#620042",
                            },
                        ],
                        "threshold": {
                            "line": {"color": "black", "width": 4},
                            "thickness": 0.75,
                            "value": 150,
                        },
                        }
                    )
                )
            )
        ]),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True, port= 8054)