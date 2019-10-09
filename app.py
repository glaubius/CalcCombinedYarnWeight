# _*_ coding: utf-8 _*_
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

length_100g = {"7 - Jumbo, Roving": (0, 50),
               "6 - Super Bulky": (50, 90),
               "5 - Bulky, Chunky, 14 ply": (90, 110),
               "4 - Medium, Worsted, Aran, 10/12 ply": (110, 240),
               "3 - Light, DK, Light Worsted, 8 ply": (240, 300),
               "2 - Fine, Sport, 4 ply": (300, 400),
               "1 - Super Fine, Fingering, 3 ply": (400, 600),
               "0 - Lace, Cobweb": (600, 10000)
              }

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[

    # Title and credits
    html.Div([
        html.H1(
            children='Yarn Weight Calculator',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
        html.H3(
            children='Want to hold multiple strands together?',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        )

    ]),


    # Inputs
    html.Div(children=[
        html.H3(
            children='Figure out the new weight here!',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),

        html.Div(className="row", children=[
            html.H5(children='Yarn 1', style={
                'textAlign': 'left',
                'color': colors['text']
                }),
            html.Div([
                html.H6(children='Weight', style={
                    'textAlign': 'left',
                    'color': colors['text']
                }),
                dcc.Input(
                    id='yarn1_weight',
                    value='', type='text',
                    style={'width': '100px'},
                    inputMode='numeric'),
                #html.Div(id='output_yarn1_weight'),
                dcc.RadioItems(
                    id='yarn1_weight_type',
                    options=[{'label': i, 'value': i} for i in ['gr', 'oz']],
                    value='gr',
                    labelStyle={'display': 'inline-block'},
                    style={'width': '48%', 'display': 'inline-block', 'fontSize': 20},

                )
            ],
            style={'width': '48%', 'display': 'table-cell'}),

            html.Div([
                html.H6(children='Length', style={
                    'textAlign': 'left',
                    'color': colors['text']
                }),
                dcc.Input(
                    id='yarn1_length',
                    value='', type='text',
                    style={'width': '100px'},
                    inputMode='numeric'),
                #html.Div(id='output_yarn1_length'),
                dcc.RadioItems(
                    id='yarn1_length_type',
                    options=[{'label': i, 'value': i} for i in ['m', 'yd']],
                    value='m',
                    labelStyle={'display': 'inline-block'},
                    style={'width': '48%', 'display': 'inline-block', 'fontSize': 20}
                )
            ],
            style={'width': '48%', 'display': 'table-cell'}),

        ]),

        html.Div(className="row", children=[
            html.H4(children='Yarn 2', style={
                'textAlign': 'left',
                'color': colors['text']
                }),
            html.Div([
                html.H6(children='Weight', style={
                    'textAlign': 'left',
                    'color': colors['text']
                }),
                dcc.Input(
                    id='yarn2_weight',
                    value='', type='text',
                    style={'width': '100px'},
                    inputMode='numeric'),
                #html.Div(id='output_yarn2_weight'),
                dcc.RadioItems(
                    id='yarn2_weight_type',
                    options=[{'label': i, 'value': i} for i in ['gr', 'oz']],
                    value='gr',
                    labelStyle={'display': 'inline-block'},
                    style={'width': '48%', 'display': 'inline-block', 'fontSize': 20}
                )
            ],style={'width': '48%', 'display': 'table-cell'}),

            html.Div([
                html.H6(children='Length', style={
                    'textAlign': 'left',
                    'color': colors['text']
                }),
                dcc.Input(
                    id='yarn2_length',
                    value='', type='text',
                    style={'width': '100px'},
                    inputMode='numeric'),
                #html.Div(id='output_yarn2_length'),
                dcc.RadioItems(
                    id='yarn2_length_type',
                    options=[{'label': i, 'value': i} for i in ['m', 'yd']],
                    value='m',
                    labelStyle={'display': 'inline-block'},
                    style={'width': '48%', 'display': 'inline-block', 'fontSize': 20}
                )

            ],
            style={'width': '48%', 'display': 'table-cell'})
            ],
        style={'paddingTop': 30})
    ]),


    # Calculate button
    html.Div(className="row", children=[
        html.Div(children=[
            html.Button(id='submit_button', n_clicks=0, children='submit',
            style={
                'textAlign': 'center',
                'color': colors['text']
            })
        ],
        style={'width': '48%', 'display': 'table-cell', 'paddingTop': 50})
    ]),

    # Output text
    html.Div(className="row", children=[
        html.H4(children='Results', style={
            'textAlign': 'left',
            'color': colors['text']
            }),
        html.Div(children=[
            html.H5(id='output_state', style={
                'textAlign': 'left',
                'color': colors['text']
            })
        ],
        style={'width': '48%', 'display': 'table-cell'})

    ]),

    # footer
    html.Div(className="row", children=[
        html.H6(children='Standard Weight is approximate based on broad categories as defined in the following links:'),
        html.H6(children='Created by Kathryn (BackstageKatKnits on Ravelry), Kristin (kristinbietsch), and Jen (bluesweatergirl)')
    ])

])


@app.callback(
    Output('output_state', 'children'),
    [Input('submit_button', 'n_clicks')],
    [State('yarn1_weight', 'value'),
    State('yarn1_weight_type', 'value'),
    State('yarn2_weight', 'value'),
    State('yarn2_weight_type', 'value'),
    State('yarn1_length', 'value'),
    State('yarn1_length_type', 'value'),
    State('yarn2_length', 'value'),
    State('yarn2_length_type', 'value')]
    )

def update_output_div(n_clicks,y1_weight, y1_weight_type, y2_weight, y2_weight_type,
    y1_length, y1_length_type, y2_length, y2_length_type):

    yarn_inputs = {1: [float(y1_weight), y1_weight_type, float(y1_length), y1_length_type],
               2: [float(y2_weight), y2_weight_type, float(y2_length), y2_length_type]}

    for (k, v) in yarn_inputs.items():
        if v[3] == 'yd':
            v[2] = v[2] * 0.9144
            v[3] = 'm'
        elif v[1] == 'oz':
            v[0] = v[0] * 28.3495
            v[1] = 'gr'
        else:
            pass

    weight_per_meter = {k:v[0]/v[2] for (k, v) in yarn_inputs.items()}

    combined_weight_per_meter = sum(weight_per_meter.values())

    meters_per_100g = 100 / combined_weight_per_meter

    min_length = {k:v for (k, v) in length_100g.items() if v[0] < meters_per_100g}

    standard_weight = [k for (k, v) in min_length.items() if v[1] > meters_per_100g]

    return u'''
        {}
        with {:.2f} meters per 100 g.
        '''.format(standard_weight, meters_per_100g)

if __name__ == '__main__':
    app.run_server(debug=True)
