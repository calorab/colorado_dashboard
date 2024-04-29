import pandas as pd
import os
import dash
from dash import Dash, html, dcc, Input, Output, callback, dash_table
import plotly.express as px 
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


dash.register_page(__name__)

#  function to get the county specific data for facts and figures
@callback(
        Output('county-table', 'data'),
        Input('county-dropdown', 'value')
)
def get_poi_data(county: str):
    formatted_county = county.upper()
    with open('data/poi_index_comp', mode='r') as f:
        df = pd.read_csv(f)

    condition = df['location_id'] == formatted_county
    filtered_df = df[condition]

    return filtered_df.to_dict('records')

def sushi_chart():
    
    with open('data/poi_index_comp', mode='r') as f:
        df = pd.read_csv(f)
    
    columns = ['location_id', 'sushi_index']
    sushi_df = df[columns]

    return sushi_df

def pet_chart():
    with open('data/poi_index_comp', mode='r') as f:
        df = pd.read_csv(f)
    
    columns = ['location_id', 'pet_vet_index', 'pet_commercial_index']
    pet_df = df[columns]

    return pet_df

def mountain_chart():
    
    with open('data/poi_index_comp', mode='r') as f:
        df = pd.read_csv(f)
    
    columns = ['location_id', 'mountain_forest_index']
    mountain_df = df[columns]


    return mountain_df


layout = html.Div([
    html.H1('Points of Interest'),
    html.Div([
        dcc.Dropdown(['Adams', 'Arapahoe', 'Boulder', 'Denver', 'Douglas', 'ElPaso', 'Jefferson', 'Larimer'], 'Denver', id='county-dropdown'), # dropdown for table below
        dash_table.DataTable(id='county-table')
    ], style={'display': 'flex', 'flex-direction': 'row'}),
    
    html.Div([
        dcc.Graph(id='mountain-forest-graph', figure=px.bar(mountain_chart(), x='location_id')), # Mountains and Forests index graph
        dcc.Graph(id='sushi-graph', figure=px.bar(sushi_chart(), x='location_id')), # Sushi index graph
         dcc.Graph(id='pet-graph', figure=px.bar(pet_chart(), x='location_id')), # chart here for Pet commercial and vets bat chart
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1})

], style={'display': 'flex', 'flex-direction': 'column', 'padding': 20, 'margin': 40, 'border-style': 'solid', 'border-color': 'lightgrey', 'border-width': '1px', 'box-shadow': '2px 4px 4px rgba(0, 0, 0, 0.4)'})


# html.Div([ 
#     html.Div( 
#         html.H5(f"{column.replace('_', ' ').capitalize()}: {value}")
#     ) for column in table_data.columns for value in table_data[column]
# ], id='county-table')