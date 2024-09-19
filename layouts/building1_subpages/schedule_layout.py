# layouts/building1_subpages/schedule_layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc

schedule_layout = html.Div([
    html.H3("Building 1 - Schedule"),
    # Add components specific to Schedule
    # For example, a calendar or timeline
    html.Div(id='schedule-content')
])
