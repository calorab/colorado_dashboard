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
   

    days_df = df[['ID', 'AVERAGE_NUMBER_CLEAR_DAYS', 'AVERAGE_NUMBER_RAINY_DAYS', 'AVERAGE_NUMBER_SNOW_DAYS']]
    return days_df

def tables_chart():

    with open('data/weather_climate') as f:
        df = pd.read_csv(f)
    
    
    low_df = df[['COUNTY_NAME', 'ANNUAL_AVERAGE_LOW_TEMP']].reset_index(drop=True)
    high_df = df[['COUNTY_NAME', 'ANNUAL_AVERAGE_HIGH_TEMP']].reset_index(drop=True)
    precip_df = df[['COUNTY_NAME', 'ANNUAL_AVERAGE_PRECIPITATION_INCHES']].reset_index(drop=True)
    snow_df = df[['COUNTY_NAME', 'ANNUAL_AVERAGE_SNOWFALL_INCHES']].reset_index(drop=True)

    return low_df, high_df, precip_df, snow_df

def pollution_chart():

    with open('data/weather_climate') as f:
        df = pd.read_csv(f)

    poll_df = df[['ID','AIR_POLLUTION_INDEX', 'PARTICULATE_MATTER_INDEX']]

    return poll_df


low_temp, high_temp, precip, snow = tables_chart()
days = days_chart()
pollution = pollution_chart()
weather = weather_chart()



layout = html.Div([
    html.H1('Weather & Climate'),
    html.Div([
        dcc.Graph(id='weather-graph', figure=px.bar(weather, x='ID', y=['WEATHER_INDEX', 'HAIL_INDEX', 'TORNADO_INDEX', 'WIND_INDEX'])), # main weather graph (hail/tornado/etc)

        dcc.Graph(id='pollute-graph', figure=px.bar(pollution, x='ID', y=['AIR_POLLUTION_INDEX', 'PARTICULATE_MATTER_INDEX'])) # pollution and particulates
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1}),
    html.Label('Temperature Ranking:'),
    html.Div([ # second row
        
        html.Div([ # left block of tables
            
            html.Div([
                html.Table([
                    html.Caption('Annual Avg Low (F)'),
                    html.Tbody([
                        html.Tr([html.Th(row['COUNTY_NAME'],style={'textAlign': 'left'}), html.Td(row['ANNUAL_AVERAGE_LOW_TEMP'],style={'textAlign': 'right'})]) for _,row in low_temp.iterrows()    
                    ])
                ], style={'margin': 40}),

                html.Table([
                    html.Caption('Annual Avg High (F)'),
                    html.Tbody([
                        html.Tr([html.Th(row['COUNTY_NAME'],style={'textAlign': 'left'}), html.Td(row['ANNUAL_AVERAGE_HIGH_TEMP'],style={'textAlign': 'right'})]) for _,row in high_temp.iterrows()                    
                    ])
                ], style={'margin': 40})
            ], style={'display': 'flex', 'flexDirection': 'row', 'padding': 30}),

            html.Div([
                html.Table([
                    html.Caption('Annual Avg Precipitation (in.)'),
                    html.Tbody([
                        html.Tr([html.Th(row['COUNTY_NAME'],style={'textAlign': 'left'}), html.Td(row['ANNUAL_AVERAGE_PRECIPITATION_INCHES'],style={'textAlign': 'right'})]) for _,row in precip.iterrows()
                        
                    ])
                ], style={'margin': 40}),

                html.Table([
                    html.Caption('Annual Avg Snow (in.)'),
                    html.Tbody([
                        html.Tr([html.Th(row['COUNTY_NAME'],style={'textAlign': 'left'}), html.Td(row['ANNUAL_AVERAGE_SNOWFALL_INCHES'],style={'textAlign': 'right'})]) for _,row in snow.iterrows()    
                    ])
                ], style={'margin': 40})
            ], style={'display': 'flex', 'flexDirection': 'row', 'padding': 30})     
        ], style={'display': 'flex', 'flexDirection': 'column'}),

        html.Div([ # second row, right block
            dcc.Graph(id='days-graph', figure=px.bar(days, x='ID', y=['AVERAGE_NUMBER_CLEAR_DAYS', 'AVERAGE_NUMBER_RAINY_DAYS', 'AVERAGE_NUMBER_SNOW_DAYS'])) 
        ], style={'display': 'flex', 'flex-direction': 'row','padding': 10, 'flex': 1})
    ], style={'display': 'flex', 'flex-direction': 'row','justifyContent': 'space-between', 'padding': 10, 'flex': 1}),
    
    

], style={'display': 'flex', 'boxSizing': 'border-box','flex-direction': 'column', 'alignItems': 'center', 'padding': 20, 'margin': 40, 'border-style': 'solid', 'border-color': 'lightgrey', 'border-width': '1px', 'box-shadow': '2px 4px 4px rgba(0, 0, 0, 0.4)'})



