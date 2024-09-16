# app.py

from flask import Flask
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

# Initialize Flask server
server = Flask(__name__)

# Initialize Dash app
app = Dash(
    __name__,
    server=server,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        'https://fonts.googleapis.com/css?family=Open+Sans&display=swap',
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'  # Font Awesome

    ],
    suppress_callback_exceptions=True
)

# Import layouts
from layouts.home_layout import home_layout
from layouts.building1_layout import building1_layout
from layouts.building2_layout import building2_layout

# Import the navigation bar
from components.navigation import navbar

# Define the app layout with the navigation bar and page content
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,  # Include the navigation bar here
    html.Div(id='page-content')
])


# app.py (continued)

# Update the page content based on URL
@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return home_layout
    elif pathname == '/building1':
        return building1_layout
    elif pathname == '/building2':
        return building2_layout
    else:
        return html.H1('404 Page Not Found')


# Import callbacks
from callbacks import home_callbacks
from callbacks import building1_callbacks
from callbacks import building2_callbacks

if __name__ == '__main__':
    app.run_server(debug=True,host='192.168.10.254',port=8051)
