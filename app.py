import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

app = Dash(
    __name__, 
    external_stylesheets=[dbc.themes.LUX], 
    use_pages=True, 
    requests_pathname_prefix='/colorado/',
    routes_pathname_prefix='/colorado/',
    serve_locally=True
)
server = app.server
load_figure_template("LUX")

# Styling for the navigation bar
navbar_style = {
    'margin': '20px 0', 
    'boxShadow': '0 4px 2px -2px gray', 
    'padding': '10px 0', 
    'background-color': 'lightgrey'
}

# Create navigation buttons
navbar = dbc.Nav(
    [dbc.NavItem(dbc.NavLink(page["name"], href=page["relative_path"], style={'text-transform': 'capitalize'})) for page in dash.page_registry.values()],
    className="nav-justified",
    style=navbar_style
)

# Layout wrapper for Dashboard
app.layout = html.Div([
    html.H5('A data pipeline and multi-page dashboard, built with Plotly/Dash, Python, SQL, Snowflake Connector & Snowpark', style={'textAlign': 'center'}),
    navbar,
    dash.page_container
], style={'display': 'flex', 'boxSizing': 'border-box', 'flexDirection': 'column'})

if __name__ == '__main__':
    app.run(debug=True)
