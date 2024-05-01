import pandas as pd
import dash
from dash import Dash, html, dcc, Input, Output, callback, dash_table
import plotly.express as px 
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/poi')

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
    sushi_df = df[['location_id', 'sushi_index']]
    return sushi_df

def pet_chart():
    with open('data/poi_index_comp', mode='r') as f:
        df = pd.read_csv(f)
    pet_df = df[['location_id', 'pet_vet_index', 'pet_commercial_index']]
    return pet_df

def mountain_chart():
    with open('data/poi_index_comp', mode='r') as f:
        df = pd.read_csv(f)
    mountain_df = df[['location_id', 'mountain_forest_index']]
    return mountain_df

# Apply consistent styling to the graphs
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

sushi = style_graph(px.bar(sushi_chart(), x='location_id', y='sushi_index', title="Sushi Index"))
pet = style_graph(px.bar(pet_chart(), x='location_id', y=['pet_vet_index', 'pet_commercial_index'], title="Pet Index"))
mountain = style_graph(px.bar(mountain_chart(), x='location_id', y='mountain_forest_index', title="Mountain and Forest Index"))

layout = html.Div([
    html.H1('Points of Interest'),
    html.Div([
        dcc.Dropdown(
            ['Adams', 'Arapahoe', 'Boulder', 'Denver', 'Douglas', 'ElPaso', 'Jefferson', 'Larimer'], 
            'Denver', 
            id='county-dropdown', 
            clearable=False, 
            style={'width': '100%', 'maxWidth': '500px', 'margin': '0 auto'}
        ),
        dash_table.DataTable(
            id='county-table',
            style_table={'maxWidth': '1500px', 'overflowX': 'auto'},
            style_cell={'minWidth': '80px', 'width': '120px', 'maxWidth': '180px'},
            style_data={'whiteSpace': 'normal', 'height': 'auto'}
        )
    ], style={'width': '100%', 'maxWidth': '1000px', 'margin': '0 auto'}),

    html.Div([
        dcc.Graph(id='mountain-forest-graph', figure=mountain),
        dcc.Graph(id='sushi-graph', figure=sushi),
        dcc.Graph(id='pet-graph', figure=pet),
    ], style={'display': 'flex', 'flex-direction': 'row', 'justifyContent': 'center','flexWrap': 'wrap','padding': 10, 'flex': 1})

], style={'display': 'flex', 'boxSizing': 'border-box', 'flex-direction': 'column', 'alignItems': 'center','padding': 20, 'margin': 'auto', 'border-style': 'solid', 'border-color': 'lightgrey', 'border-width': '1px', 'box-shadow': '2px 4px 4px rgba(0, 0, 0, 0.4)'})

if __name__ == '__main__':
    app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=True)
    app.run(debug=True)
