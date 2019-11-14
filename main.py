import datetime
import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly
import random
import plotly.graph_objs as go
from collections import deque

app = dash.Dash()
app.layout = html.Div(
    [

        dcc.Graph(id='live-graph', animate=False),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ]
)


@app.callback(Output('live-graph', 'figure'),
               [Input('graph-update', 'n_intervals')])
def update_graph_scatter(n):
    input = pd.read_csv('data.csv', header=None)
    input = input.iloc[:, lambda df: [0, 1, 27]]
    # input = np.array(input)
    #print(input[1], input[27])
    X = input[1]
    Y = input[27]/1000

    data = plotly.graph_objs.Scatter(
                x=list(X),
                y=list(Y),
                name='Scatter',
                mode='lines+markers'
                )

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                yaxis=dict(range=[min(Y), max(Y)]),
                                                title="Display CPU Temperature",
                                                xaxis_title="Time",
                                                yaxis_title="Temperature",)}


if __name__ == '__main__':
    app.run_server(debug=True)

