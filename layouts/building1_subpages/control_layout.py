# layouts/building1_subpages/control_layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc

control_layout = html.Div([
    html.H3("Building 1 - Control"),
    # Add components specific to Control
    # For example, control panels or buttons
    html.Div(id='control-content')
])
