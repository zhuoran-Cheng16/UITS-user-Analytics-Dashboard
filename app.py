# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go



external_stylesheets = ['styles.css']

app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.Div([

    html.Div(children='''
        Updates are recieved every 5 mins
    '''),

    html.Div([
        html.Div([
            html.Div(
            [html.H6(id="well_text2"), html.P("No. of notifications")],
                                    id="wells5",
                                    className="mini_container",

                    ),
            html.Div(
            [html.H6(id="well_text3"), html.P("No. of notifications")],
                                    id="wells4",
                                    className="mini_container",

                    ),
            html.Div(
            [html.H6(id="well_text4"), html.P("No. of notifications")],
                                    id="wells3",
                                    className="mini_container",

                    ),
            html.Div(
            [html.H6(id="well_text"), html.P("No. of notifications")],
                                    id="wells2",
                                    className="mini_container",

                    ),
            html.Div(
            [html.H6(id="gasText"), html.P("No of compliance errors")],
                        id="gas",
                        className="mini_container",
                    ),
            html.Div(
            [html.H6(id="oilText"), html.P("No of printer for this hours")],
                        id="oil",
                        className="mini_container",
                    ),
            ],

        id="info-container",
            className="row container-display",
                        ),

    ], className="row flex-display")

], className = "row"),
    html.Div([
        html.Div([


        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization',
                    'height': '500',

                }
            }
        ),

    ], className = 'four columns'),


    html.Div([
         dcc.Graph(id='device_usage',
                       figure=go.Figure(
                           data=[go.Pie(labels=['Desktop', 'Mobile', 'Tablet'],
                                        values=['42344', '1864', '2390'])],
                           layout=go.Layout(
                               title='Device Usage',
                               height=int(500),
                               ),

                       ))    ], className="four columns",
        style={"margin-left": "10px"},
    ),


    html.Div([
        dcc.Graph(
            id='example-graph-3',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization',
                    'height': '500',
                    'width' : '500',

                }
            }
        )
        ], className = 'four columns')
            ], className = 'row'),

html.Div([
    dcc.Graph(
    figure=dict(
        data=[
            dict(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                   350, 430, 474, 526, 488, 537, 500, 439],
                name='Rest of world',
                marker=dict(
                    color='rgb(55, 83, 109)'
                )
            ),
            dict(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                   299, 340, 403, 549, 499],
                name='China',
                marker=dict(
                    color='rgb(26, 118, 255)'
                )
            )
        ],
        layout=dict(
            title='US Export of Plastic Scrap',
            showlegend=True,
            legend=dict(
                x=0,
                y=1.0
            ),
            margin=dict(l=40, r=0, t=40, b=30)
        )
    ),
    style={'height': 300, 'margin': 10},
    id='my-graph'
    )

    ]),



])
if __name__ == '__main__':
    app.run_server(debug=True)
