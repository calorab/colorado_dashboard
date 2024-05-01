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
    return df[columns]

def days_chart():
    with open('data/weather_climate') as f:
        df = pd.read_csv(f)
    return df[['ID', 'AVERAGE_NUMBER_CLEAR_DAYS', 'AVERAGE_NUMBER_RAINY_DAYS', 'AVERAGE_NUMBER_SNOW_DAYS']]

def tables_chart():
    with open('data/weather_climate') as f:
        df = pd.read_csv(f)
    return (
        df[['COUNTY_NAME', 'ANNUAL_AVERAGE_LOW_TEMP']].reset_index(drop=True),
        df[['COUNTY_NAME', 'ANNUAL_AVERAGE_HIGH_TEMP']].reset_index(drop=True),
        df[['COUNTY_NAME', 'ANNUAL_AVERAGE_PRECIPITATION_INCHES']].reset_index(drop=True),
        df[['COUNTY_NAME', 'ANNUAL_AVERAGE_SNOWFALL_INCHES']].reset_index(drop=True)
    )

def pollution_chart():
    with open('data/weather_climate') as f:
        df = pd.read_csv(f)
    return df[['ID','AIR_POLLUTION_INDEX', 'PARTICULATE_MATTER_INDEX']]

def style_graph(figure, top_margin=80):
    figure.update_layout(
        paper_bgcolor='rgba(255,255,255,0.95)',
        plot_bgcolor='rgba(255,255,255,1)',
        margin=dict(l=40, r=40, t=top_margin, b=40),
        title_font=dict(size=20, color='darkblue'),
        font=dict(family="Lato, sans-serif", size=12, color='black'),
        xaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
        yaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        barmode='group'
    )
    figure.update_traces(marker_line_width=1, marker_line_color='navy')
    return figure

low_temp, high_temp, precip, snow = tables_chart()
days = days_chart()
pollution = pollution_chart()
weather = weather_chart()

layout = html.Div([
    html.H1('Weather & Climate'),
    html.Div([
        dcc.Graph(id='weather-graph', figure=style_graph(px.bar(weather, x='ID', y=['WEATHER_INDEX', 'HAIL_INDEX', 'TORNADO_INDEX', 'WIND_INDEX'], title='Main Weather Indices'))),
        dcc.Graph(id='pollute-graph', figure=style_graph(px.bar(pollution, x='ID', y=['AIR_POLLUTION_INDEX', 'PARTICULATE_MATTER_INDEX'], title='Pollution Indices')))
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1}),
    html.Label('Temperature Ranking:', style={'fontSize': 20, 'margin': '20px 0'}),
    html.Div([ 
        html.Div([ 
            html.Div([
                html.Table([
                    html.Caption('Annual Avg Low (F)', style={'fontSize': 18}),
                    html.Tbody([
                        html.Tr([html.Th(row['COUNTY_NAME'],style={'textAlign': 'left', 'fontWeight': 'bold'}), html.Td(row['ANNUAL_AVERAGE_LOW_TEMP'],style={'textAlign': 'right'})]) for _,row in low_temp.iterrows()
                    ])
                ], style={'margin': 40}),
                html.Table([
                    html.Caption('Annual Avg High (F)', style={'fontSize': 18}),
                    html.Tbody([
                        html.Tr([html.Th(row['COUNTY_NAME'],style={'textAlign': 'left', 'fontWeight': 'bold'}), html.Td(row['ANNUAL_AVERAGE_HIGH_TEMP'],style={'textAlign': 'right'})]) for _,row in high_temp.iterrows()
                    ])
                ], style={'margin': 40})
            ], style={'display': 'flex', 'flexDirection': 'row', 'padding': 30}),
            html.Div([
                html.Table([
                    html.Caption('Annual Avg Precipitation (in.)', style={'fontSize': 18}),
                    html.Tbody([
                        html.Tr([html.Th(row['COUNTY_NAME'],style={'textAlign': 'left', 'fontWeight': 'bold'}), html.Td(row['ANNUAL_AVERAGE_PRECIPITATION_INCHES'],style={'textAlign': 'right'})]) for _,row in precip.iterrows()
                    ])
                ], style={'margin': 40}),
                html.Table([
                    html.Caption('Annual Avg Snow (in.)', style={'fontSize': 18}),
                    html.Tbody([
                        html.Tr([html.Th(row['COUNTY_NAME'],style={'textAlign': 'left', 'fontWeight': 'bold'}), html.Td(row['ANNUAL_AVERAGE_SNOWFALL_INCHES'],style={'textAlign': 'right'})]) for _,row in snow.iterrows()
                    ])
                ], style={'margin': 40})
            ], style={'display': 'flex', 'flexDirection': 'row', 'padding': 30})     
        ], style={'display': 'flex', 'flexDirection': 'column'}),
        html.Div([
            dcc.Graph(id='days-graph', figure=style_graph(px.bar(days, x='ID', y=['AVERAGE_NUMBER_CLEAR_DAYS', 'AVERAGE_NUMBER_RAINY_DAYS', 'AVERAGE_NUMBER_SNOW_DAYS'], title='Average Days'), top_margin=120))
        ], style={'padding': 10, 'flex': 1})
    ], style={'display': 'flex', 'flex-direction': 'row','justifyContent': 'space-between', 'padding': 10, 'flex': 1})
], style={'display': 'flex', 'boxSizing': 'border-box','flex-direction': 'column', 'alignItems': 'center', 'padding': 20, 'margin': 'auto', 'border-style': 'solid', 'border-color': 'lightgrey', 'border-width': '1px', 'box-shadow': '2px 4px 4px rgba(0, 0, 0, 0.4)'})

if __name__ == '__main__':
    app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=True)
    app.run(debug=True)


