import pandas as pd
import dash
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px 
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

dash.register_page(__name__)

def graph_data():
    with open('data/demographics') as f:
        df = pd.read_csv(f)

    locations = df['LOCATION_ID']
    pop_now = df['POPULATION_2020']
    pop_5yr = df['POPULATION_5YR_PROJ']
    med_income = df['HH_MEDIAN_INCOME']
    urban_pop = df['POPULATION_URBAN']
    rural_pop = df['POPULATINO_RURAL']
    house_cpi = df['CPI_HOUSING']
    crime = df['CRIME_INDEX']
    cpi = df['CONSUMER_PRICE_INDEX']

layout = html.Div([
    html.H1('Key Demographics'),
    html.Div([
        dcc.Graph(), # population
        dcc.Graph() # HH median Income
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1}),
    html.Div([
        dcc.Graph(), # Urban V Rural Population
        dcc.Graph() # Housing (CPI/ETC?)
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1}),
    html.Div([
        dcc.Graph(), # Crime index (murder/burglury?)
        dcc.Graph() # CPI
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1})

], style={'display': 'flex', 'flex-direction': 'column', 'padding': 20, 'margin': 40, 'border-style': 'solid', 'border-color': 'lightgrey', 'border-width': '1px', 'box-shadow': '2px 4px 4px rgba(0, 0, 0, 0.4)'})



