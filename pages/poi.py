import pandas
import dash
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px 
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


dash.register_page(__name__)


layout = html.Div([
    html.H1('Points of Interest'),
    html.Div([
        dcc.Graph(), # chart here for Pet commercial and vets bat chart
        html.div([
            dcc.Dropdown(), # dropdown for table below

            html.Table([
                html.Thead(
                    html.Tr([html.Td(cons_df.columns[0]), html.Td(cons_df.columns[1])])
                ),
                html.Tbody([
                    html.Tr([html.Th(cons_df.iloc[0, 0]), html.Td(cons_df.iloc[0, 1])]),
                    html.Tr([html.Th(cons_df.iloc[1, 0]), html.Td(cons_df.iloc[1, 1])]),
                    html.Tr([html.Th(cons_df.iloc[2, 0]), html.Td(cons_df.iloc[2, 1])]),
                    html.Tr([html.Th(cons_df.iloc[3, 0]), html.Td(cons_df.iloc[3, 1])]),
                    html.Tr([html.Th(cons_df.iloc[4, 0]), html.Td(cons_df.iloc[4, 1])])
                ], style={'padding': 10, 'flex': 1, 'textAlign': 'left'})
            ])
        ], style={'display': 'flex', 'flex-direction': 'column'})
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1}),
    html.Div([
        dcc.Graph(), # Mountains and Forests index graph
        dcc.Graph() # Sushi index graph
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1})

], style={'display': 'flex', 'flex-direction': 'column', 'padding': 20, 'margin': 40, 'border-style': 'solid', 'border-color': 'lightgrey', 'border-width': '1px', 'box-shadow': '2px 4px 4px rgba(0, 0, 0, 0.4)'})