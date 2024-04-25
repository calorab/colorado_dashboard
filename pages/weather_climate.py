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
    
    columns = ['ID', 'WEATHER_INDEX', 'HAIL_INDEX', 'TORNADO_INDEX', 'WIND_INDEX']
    weather = df[columns]

    return weather

def days_chart():
    with open('data/weather_climate') as f:
        df = pd.read_csv(f)
    
    columns = ['AVERAGE_NUMBER_CLEAR_DAYS', 'AVERAGE_NUMBER_RAINY_DAYS', 'AVERAGE_NUMBER_SNOW_DAYS']

    days_df = df[columns]
    return days_df

def tables_chart():

    with open('data/weather_climate') as f:
        df = pd.read_csv(f)
    
    
    low_df = df['COUNTY_NAME', 'ANNUAL_AVERAGE_LOW_TEMP']
    high_df = df['COUNTY_NAME', 'ANNUAL_AVERAGE_HIGH_TEMP']
    precip_df = df['COUNTY_NAME', 'ANNUAL_AVERAGE_PRECIPITATION_INCHES']
    snow_df = df['COUNTY_NAME', 'ANNUAL_AVERAGE_SNOWFALL_INCHES']

    return low_df, high_df, precip_df, snow_df

low_temp, high_temp, precip, snow = tables_chart()

def pollution_chart():

    with open('data/weather_climate') as f:
        df = pd.read_csv(f)

    poll_df = df['ID','AIR_POLLUTION_INDEX', 'PARTICULATE_MATTER_INDEX']

    return poll_df

layout = html.Div([
    html.H1('Weather & Climate'),
    html.Div([
        dcc.Graph(id='weather-graph', figure=px.bar(weather_chart(), y='Weather Index (2020)')), # main weather graph (hail/tornado/etc)

         dcc.Graph(id='pollute-graph', figure=px.bar(pollution_chart(), y='Pollution Index (2020)')) # pollution and particulates
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1}),
    
    html.Div([ # second row
        html.Div([ # left block of tables
            html.Label('Temperature Ranking:'),
            html.Table([
                html.Caption('Annual Avg Low (F)'),
                html.Tbody([
                    html.Tr([html.Th(row['COUNTY_NAME']), html.Td(row['ANNUAL_AVERAGE_LOW_TEMP'])]) for row in low_temp.iterrows()
                    
                ], style={'padding': 10, 'flex': 1, 'textAlign': 'left'})
            ]),
            html.Table([
                html.Caption('Annual Avg High (F)'),
                html.Tbody([
                    html.Tr([html.Th(row['COUNTY_NAME']), html.Td(row['ANNUAL_AVERAGE_HIGH_TEMP'])]) for row in high_temp.iterrows()
                    
                ], style={'padding': 10, 'flex': 1, 'textAlign': 'left'})
            ]),
            html.Table([
                html.Caption('Annual Avg Precipitation (in.)'),
                html.Tbody([
                    html.Tr([html.Th(row['COUNTY_NAME']), html.Td(row['ANNUAL_AVERAGE_PRECIPITATION_INCHES'])]) for row in precip.iterrows()
                    
                ], style={'padding': 10, 'flex': 1, 'textAlign': 'left'})
            ]),html.Table([
                html.Caption('Annual Avg Snow (in.)'),
                html.Tbody([
                    html.Tr([html.Th(row['COUNTY_NAME']), html.Td(row['ANNUAL_AVERAGE_PRECIPITATION_INCHES'])]) for row in snow.iterrows()
                    
                ], style={'padding': 10, 'flex': 1, 'textAlign': 'left'})
            ])
        ], style={}),

        html.Div([ # second row, right block
            dcc.Graph(id='days-graph', figure=px.bar(days_chart(), y='# of days in a year (2020)')) 
        ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1})
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1}),
    
    

], style={'display': 'flex', 'flex-direction': 'column', 'padding': 20, 'margin': 40, 'border-style': 'solid', 'border-color': 'lightgrey', 'border-width': '1px', 'box-shadow': '2px 4px 4px rgba(0, 0, 0, 0.4)'})



