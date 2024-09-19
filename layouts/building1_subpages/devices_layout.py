# layouts/building1_subpages/devices_layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc

devices_layout = html.Div([
    html.H3("Building 1 - Devices Info"),
    # Add components specific to Devices Info
    # For example, a table or graphs showing device statuses
    html.Div(id='devices-content')
])
