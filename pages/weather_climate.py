import pandas as pd
import dash
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px 
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


dash.register_page(__name__, path='/')


def weather_chart():
    with open('data/weather_climate') as f:
        df = pd.read_csv(f)
    
    locations = df['ID']
    weather = df['WEATHER_INDEX']
    hail = df['HAIL_INDEX']
    tornado = df['TORNADO_INDEX']
    wind = df['WIND_INDEX']

    return locations, weather, hail, tornado, wind

def days_chart():
    with open('data/weather_climate') as f:
        df = pd.read_csv(f)
    
    locations = df['ID']
    clear = df['AVERAGE_NUMBER_CLEAR_DAYS']
    rain = df['AVERAGE_NUMBER_RAINY_DAYS']
    snow = df['AVERAGE_NUMBER_SNOW_DAYS']

    return locations, clear, rain, snow

def tables_chart():

    with open('data/weather_climate') as f:
        df = pd.read_csv(f)
    
    avg_low = df['ANNUAL_AVERAGE_LOW_TEMP']
    avg_high = ['ANNUAL_AVERAGE_HIGH_TEMP']
    avg_precip = df['ANNUAL_AVERAGE_PRECIPITATION_INCHES']
    avg_snow = df['ANNUAL_AVERAGE_SNOWFALL_INCHES']

    return avg_low, avg_high, avg_precip, avg_snow

def pollution_chart():

    with open('data/weather_climate') as f:
        df = pd.read_csv(f)

    poll = df['IR_POLLUTION_INDEX']
    part = df['PARTICULATE_MATTER_INDEX']

    return poll, part

layout = html.Div([
    html.H1('Weather & Climate'),
    html.Div([
        dcc.Graph(), # main weather graph (hail/tornado/etc)

         dcc.Graph() # pollution and particulates
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1}),
    
    html.Div([ # second row
        html.Div([ # left block of tables
            html.Label('Temperature Ranking:'),
            html.Table([
                html.Caption('Annual Avg Low (F)'),
                html.Tbody([
                    html.Tr([html.Th(cons_df.iloc[0, 0]), html.Td(cons_df.iloc[0, 1])]),
                    html.Tr([html.Th(cons_df.iloc[1, 0]), html.Td(cons_df.iloc[1, 1])]),
                    html.Tr([html.Th(cons_df.iloc[2, 0]), html.Td(cons_df.iloc[2, 1])]),
                    html.Tr([html.Th(cons_df.iloc[3, 0]), html.Td(cons_df.iloc[3, 1])]),
                    html.Tr([html.Th(cons_df.iloc[4, 0]), html.Td(cons_df.iloc[4, 1])])
                ], style={'padding': 10, 'flex': 1, 'textAlign': 'left'})
            ]),
            html.Table([
                html.Caption('Annual Avg High (F)'),
                html.Tbody([
                    html.Tr([html.Th(cons_df.iloc[0, 0]), html.Td(cons_df.iloc[0, 1])]),
                    html.Tr([html.Th(cons_df.iloc[1, 0]), html.Td(cons_df.iloc[1, 1])]),
                    html.Tr([html.Th(cons_df.iloc[2, 0]), html.Td(cons_df.iloc[2, 1])]),
                    html.Tr([html.Th(cons_df.iloc[3, 0]), html.Td(cons_df.iloc[3, 1])]),
                    html.Tr([html.Th(cons_df.iloc[4, 0]), html.Td(cons_df.iloc[4, 1])])
                ], style={'padding': 10, 'flex': 1, 'textAlign': 'left'})
            ]),
            html.Table([
                html.Caption('Annual Avg Precipitation (in.)'),
                html.Tbody([
                    html.Tr([html.Th(cons_df.iloc[0, 0]), html.Td(cons_df.iloc[0, 1])]),
                    html.Tr([html.Th(cons_df.iloc[1, 0]), html.Td(cons_df.iloc[1, 1])]),
                    html.Tr([html.Th(cons_df.iloc[2, 0]), html.Td(cons_df.iloc[2, 1])]),
                    html.Tr([html.Th(cons_df.iloc[3, 0]), html.Td(cons_df.iloc[3, 1])]),
                    html.Tr([html.Th(cons_df.iloc[4, 0]), html.Td(cons_df.iloc[4, 1])])
                ], style={'padding': 10, 'flex': 1, 'textAlign': 'left'})
            ]),html.Table([
                html.Caption('Annual Avg Snow (in.)'),
                html.Tbody([
                    html.Tr([html.Th(cons_df.iloc[0, 0]), html.Td(cons_df.iloc[0, 1])]),
                    html.Tr([html.Th(cons_df.iloc[1, 0]), html.Td(cons_df.iloc[1, 1])]),
                    html.Tr([html.Th(cons_df.iloc[2, 0]), html.Td(cons_df.iloc[2, 1])]),
                    html.Tr([html.Th(cons_df.iloc[3, 0]), html.Td(cons_df.iloc[3, 1])]),
                    html.Tr([html.Th(cons_df.iloc[4, 0]), html.Td(cons_df.iloc[4, 1])])
                ], style={'padding': 10, 'flex': 1, 'textAlign': 'left'})
            ])
        ], style={}),

        html.Div([ # second row, right block
            dcc.Graph() # stacked bar chart, virtical clear/rainy/snow days
        ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1})
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1}),
    
    

], style={'display': 'flex', 'flex-direction': 'column', 'padding': 20, 'margin': 40, 'border-style': 'solid', 'border-color': 'lightgrey', 'border-width': '1px', 'box-shadow': '2px 4px 4px rgba(0, 0, 0, 0.4)'})



