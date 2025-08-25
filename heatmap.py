import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

#df = px.data.medals_wide(indexed=True)
df = pd.read_csv("pm1jaj.csv")
dff = pd.read_csv("sample.csv")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Months included:"),
    dcc.Checklist(
        id='medals',
        options=[{'label': x, 'value': x} 
                 for x in df.columns],
        value=df.columns.tolist(),
    ),
    #dcc.Graph(id="graph"),
    dcc.Tab(label='Heat Map', children=[
            dcc.Graph(id="graph"),
        ]),
    dcc.Tab(label='PM2.5', children=[
            dcc.Graph(
                figure=px.bar(df, y=['jan', 'apr', 'aug'])
            )
        ]),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("medals", "value")])
def filter_heatmap(cols):
    fig = px.imshow(df[cols])
    return fig

app.run_server(debug=True, port= 8053)