import pandas as pd
import dash
from dash import Dash, html, dcc, Input, Output, callback, dash_table
import plotly.express as px 
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


dash.register_page(__name__, path='/county')


@callback(
       Output('main-table', 'data'), # sector data for table
       Input('sector-dropdown', 'value') # dropdown for sector choice
       )
def generate_table(sector):
    
    with open('data/counties', mode='r') as f:
        df = pd.read_csv(f)
    
    wc_cols = ['WEATHER_INDEX', 'ANNUAL_AVERAGE_SNOWFALL_INCHES', 'AVERAGE_NUMBER_SNOW_DAYS','AVERAGE_NUMBER_RAINY_DAYS', 'ANNUAL_AVERAGE_HIGH_TEMP', 'ANNUAL_AVERAGE_LOW_TEMP', 'AIR_POLLUTION_INDEX']
    pop_cols = ['DIVERSITY_PCT', 'POPULATION_DENSITY', 'POPULATION_2020', 'POPULATION_5YR_PROJ', 'OCCUPATION_WHITE_COLLAR', 'OCCUPATION_BLUE_COLLAR']
    hh_cols = ['HOUSING_OWNER_MEDIAN_VALUE_2020', 'HOUSING_MEDIAN_RENT', 'HOUSING_SINGLE_UNIT_PCT', 'CPI_HOUSING', 'CONSUMER_PRICE_INDEX', 'HH_AVG_INCOME', 'HH_MEDIAN_INCOME', 'HH_PCT_WO_CHILDREN']
    
    sector_dict = {'Weather & Climate': df[wc_cols], 'Population': df[pop_cols], 'Households': df[hh_cols]}

    table_data = sector_dict[sector]
    
    return table_data.to_dict('records')
    


layout = html.Div([
    html.H1('County Level Details'),
    dcc.Dropdown(['Weather & Climate', 'Population', 'Households'], 'Population', id='sector-dropdown', style={'margin-top': 10}), 
    dash_table.DataTable(id='main-table') # possibly go back to using a function here??
], style={'display': 'flex', 'flex-direction': 'column', 'padding': 20, 'margin': 40, 'border-style': 'solid', 'border-color': 'lightgrey', 'border-width': '1px', 'box-shadow': '2px 4px 4px rgba(0, 0, 0, 0.4)'})


