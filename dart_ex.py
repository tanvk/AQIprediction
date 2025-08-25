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

#app = dash.react.Dash('Hello World')

df = pd.read_csv("sample.csv")
#df = df.groupby(['created_at', 'PM1', 'PM2', 'PM4', 'PM10']).mean()

df.reset_index(inplace=True)
print(df[:5])

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([

    html.Div([
            html.H1(children='AIR QUALITY OF PUNE',
                    style = {'textAlign' : 'center'}
            )],
            className="app-header--title",
            style = {'padding-top' : '1%'}
        ),
    #html.Button(dcc.link("HOME"))#, id='btn-nclicks-1', n_clicks=0),
    #html.Button(dcc.Link("back", href=f"http://127.0.0.1:5000/"), className='three columns'),
    #dcc.Link(html.Button('back'), href=f"http://127.0.0.1:5000/forecast"),

    #dcc.Link(html.Button('HOME'), href="http://127.0.0.1:5000"),
    #dcc.Link("HOME", href=f"http://127.0.0.1:5000/"),
    #dcc.Location(id='url', refresh=False),
    #dcc.Link('HOME', href='/forecast'),
    #html.Div(id='page-content'),'''
    
    html.H2("Choose Pollutant:", style={'text-align': 'left'}, className="app-header--title"),

    dcc.Dropdown(id="slect_pollutant",
                 options=[
                     {"label": "PM1.0", "value": 1},
                     {"label": "PM2.5", "value": 2},
                     {"label": "PM4.0", "value": 3},
                     {"label": "PM10.0", "value": 4}],
                 multi=False,
                 value=1,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    html.Div([], className = 'col-2'),
    
    dcc.Graph(id='graph', figure={})

])

@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='slect_pollutant', component_property='value')]
)
def update_graph(option_slctd):
    dff = df.copy()
    if option_slctd == 1:
        plot_data = [go.Scatter(x = dff.created_at, y = dff.PM1, mode = 'markers')]
    elif option_slctd == 2:
        plot_data = [go.Scatter(x = dff.created_at, y = dff.PM2, mode = 'markers')]
    elif option_slctd == 3:
        plot_data = [go.Scatter(x = dff.created_at, y = dff.PM4, mode = 'markers')]
    elif option_slctd == 4:
        plot_data = [go.Scatter(x = dff.created_at, y = dff.PM10, mode = 'markers')]
    
    plot_layout = go.Layout(title = "Pollutant based Graphs")

    fig = go.Figure(data = plot_data, layout = plot_layout)

    return fig

'''@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    return html.Div([
        html.H3('You are on page {}'.format(pathname))
    ])'''


if __name__ == '__main__':
    app.run_server(debug=True)