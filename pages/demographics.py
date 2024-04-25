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

    
    pop_df = df['LOCATION_ID', 'POPULATION_2020', 'POPULATION_5YR_PROJ']
    hh_df = df['LOCATION_ID','HH_MEDIAN_INCOME']
    popdist_df = df['LOCATION_ID','POPULATION_URBAN', 'POPULATINO_RURAL']
    house_df = df['LOCATION_ID','CPI_HOUSING']
    crime_df = df['LOCATION_ID','CRIME_INDEX']
    cpi_df = df['LOCATION_ID','CONSUMER_PRICE_INDEX']

    return pop_df, popdist_df, house_df, crime_df, cpi_df, hh_df

pop, popdist, house, crime, cpi, household = graph_data()

layout = html.Div([
    html.H1('Key Demographics'),
    html.Div([
        dcc.Graph(id='pop-graph', figure=px.bar(pop, y='population')), # population
        dcc.Graph(id='hh-graph', figure=px.bar(household, y='# of households (2020)')) # HH median Income
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1}),
    html.Div([
        dcc.Graph(id='popdist-graph', figure=px.bar(popdist, y='population (2020)')), # Urban V Rural Population
        dcc.Graph(id='house-graph', figure=px.bar(house, y='Home CPI (2020)')) # Housing (CPI/ETC?)
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1}),
    html.Div([
        dcc.Graph(id='crime-graph', figure=px.bar(crime, y='Crime Index (2020)')), # Crime index (murder/burglury?)
        dcc.Graph(id='cpi-graph', figure=px.bar(cpi, y='Consumer Price Index (2020)')) # CPI
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1})

], style={'display': 'flex', 'flex-direction': 'column', 'padding': 20, 'margin': 40, 'border-style': 'solid', 'border-color': 'lightgrey', 'border-width': '1px', 'box-shadow': '2px 4px 4px rgba(0, 0, 0, 0.4)'})



