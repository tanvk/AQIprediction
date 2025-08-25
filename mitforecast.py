import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import date

app = dash.Dash()

df = pd.read_csv("mit1.csv")
df["created_at"] = pd.to_datetime(df["created_at"])

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df["created_at"],
        y=df["PM25"],
        fill="tozeroy",
        fillcolor="indigo",
        name="PM2.5",
    )
)
fig.add_trace(
    go.Scatter(x=df["created_at"], y=df["PM1.0"], fill="tonexty", name="PM1.0")
)
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1day", step="day", stepmode="backward"),
                    dict(count=7, label="7days", step="day", stepmode="backward"),
                    dict(count=15, label="15days", step="day", stepmode="todate"),
                    dict(count=21, label="21days", step="day", stepmode="backward"),
                    dict(step="all"),
                ]
            )
        ),
        rangeslider=dict(visible=True),
        type="date",
    )
)
fig.update_layout(title="P.M wrt Time at MIT,PUNE")

app.layout = html.Div([dcc.Graph(figure=fig)])

app.run_server(debug=True, use_reloader=False, port=8055)