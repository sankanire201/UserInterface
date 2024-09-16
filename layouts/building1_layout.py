# layouts/building1_layout.py
import dash_bootstrap_components as dbc
from dash import html

building1_layout = dbc.Container([
    html.H2("Building 1 Dashboard"),
    # Add more components specific to Building 1
], fluid=True)
