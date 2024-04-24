import pandas
import dash
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px 
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=True)
# logging.basicConfig(filename='api_calls.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(message)s')
server = app.server
load_figure_template("LUX")

app.layout = html.Div([html.H1('Multi-page app with Dash Pages'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]), 
    
    dash.page_container
])


if __name__ == '__main__':
    app.run(debug=True)
# app.run_server(dev_tools_hot_reload=False) to remove hot-reloading
# The location of the app: http://127.0.0.1:8050/ 