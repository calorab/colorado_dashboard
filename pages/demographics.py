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

    pop_df = df[['LOCATION_ID', 'POPULATION_2020', 'POPULATION_5YR_PROJ']]
    hh_df = df[['LOCATION_ID','HH_MEDIAN_INCOME']]
    popdist_df = df[['LOCATION_ID','POPULATION_URBAN', 'POPULATION_RURAL']]
    house_df = df[['LOCATION_ID','CPI_HOUSING']]
    crime_df = df[['LOCATION_ID','CRIME_INDEX']]
    cpi_df = df[['LOCATION_ID','CONSUMER_PRICE_INDEX']]

    return pop_df, popdist_df, house_df, crime_df, cpi_df, hh_df

pop, popdist, house, crime, cpi, household = graph_data()

# Styling function for Plotly graphs
def style_graph(figure):
    figure.update_layout(
        paper_bgcolor='rgba(255,255,255,0.95)',
        plot_bgcolor='rgba(255,255,255,1)',
        margin=dict(l=40, r=40, t=40, b=40),
        title_font=dict(size=20, color='darkblue'),
        font=dict(family="Lato, sans-serif", size=12, color='black'),
        xaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
        yaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    figure.update_traces(marker_line_width=1, marker_line_color='navy')
    return figure

# Apply styles to each graph
layout = html.Div([
    html.H1('Key Demographics'),
    html.Div([
        dcc.Graph(id='pop-graph', figure=style_graph(px.bar(pop, x='LOCATION_ID', y=['POPULATION_2020', 'POPULATION_5YR_PROJ'], title='Population Overview'))),
        dcc.Graph(id='hh-graph', figure=style_graph(px.bar(household, x='LOCATION_ID', y='HH_MEDIAN_INCOME', title='Household Median Income')))
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex-wrap': 'wrap', 'justify-content': 'center'}),
    html.Div([
        dcc.Graph(id='popdist-graph', figure=style_graph(px.bar(popdist, x='LOCATION_ID', y=['POPULATION_URBAN', 'POPULATION_RURAL'], title='Urban vs Rural Population'))),
        dcc.Graph(id='house-graph', figure=style_graph(px.bar(house, x='LOCATION_ID', y='CPI_HOUSING', title='Housing CPI')))
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex-wrap': 'wrap', 'justify-content': 'center'}),
    html.Div([
        dcc.Graph(id='crime-graph', figure=style_graph(px.bar(crime, x='LOCATION_ID', y='CRIME_INDEX', title='Crime Index'))),
        # Uncomment the next line if you want to include the CPI graph
        # dcc.Graph(id='cpi-graph', figure=style_graph(px.bar(cpi, x='LOCATION_ID', y='CONSUMER_PRICE_INDEX', title='Consumer Price Index')))
    ], style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex-wrap': 'wrap', 'justify-content': 'center'})

], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'padding': 20, 'margin': 'auto', 'max-width': '1200px', 'border-style': 'solid', 'border-color': 'lightgrey', 'border-width': '1px', 'box-shadow': '2px 4px 4px rgba(0, 0, 0, 0.4)'})

if __name__ == '__main__':
    app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=True)
    app.run(debug=True)
