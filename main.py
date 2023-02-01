import dash
from dash import html
from dash import dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([html.H1('This is my first Python Dashboard!')]),
    html.Div([
        dcc.Graph(
            id='Graph',
            figure={'data': [{'x': [1, 2, 3, 4, 6, 3, 4, 5, 6],
                              'y': [1, 2, 3, 4, 6, 3, 4, 5, 6],
                              'type': 'line',
                              'marker': {'color': 'green'},
                              'line': {'width': 17}}],
                    'layout': {'title': 'My First Graph',
                               'xaxis': {'title': 'Value'},
                               'yaxis': {'title': 'Another Value'}}}
        ),
    ], style={'width': '30%'})
])


if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8080, debug=True)
