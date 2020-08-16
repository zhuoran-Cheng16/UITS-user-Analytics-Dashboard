import dash
import dash_core_components as dcc
import dash_html_components as html
import chart_studio.plotly as py
import plotly.graph_objs as go

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

dataPieChart = [
{
"values": [[10, 90], [5, 95], [15, 85], [20, 80]],
"type": "pie",
},
]

app.layout = html.Div(
children=[

    # charts
    html.Div([

        html.Div([
            dcc.Graph(
                id='figure1',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ], className="four columns",
           style={"margin-left": "30px"},
        ),


        html.Div([
             dcc.Graph(id='device_usage',
                           figure=go.Figure(
                               data=[go.Pie(labels=['Desktop', 'Mobile', 'Tablet'],
                                            values=['42344', '1864', '2390'])],
                               layout=go.Layout(
                                   title='Device Usage')
                           ))    ], className="four columns",
            style={"margin-left": "10px"},
        ),

    ],
        className="row"
    ),
],
className="row",
style={"margin": "0%"},
)

if __name__ == '__main__':
    app.run_server(debug=True)
