# layouts/home_layout.py

import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px

# Placeholder data
data = {
    'Building': ['Building 1', 'Building 2'],
    'Consumption': [0, 0]
}
fig = px.bar(data, x='Consumption', y='Building', orientation='h')

home_layout = dbc.Container([
    html.Div(style={'height': '30px'}),  # Spacer

    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    html.H5([
                        html.I(className="fas fa-chart-bar"),  # Icon for Building Consumption
                        html.Span(" Building Consumption", className='ml-2')
                    ], className='card-title'),
                    className='card-header'
                ),
                dbc.CardBody(
                    dcc.Graph(id='consumption-chart', figure=fig)
                ),
            ], className='card mb-4 shadow'),
            width=4
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    html.H5([
                        html.I(className="fas fa-bolt"),  # Icon for Grid Status
                        html.Span(" Grid Status", className='ml-2')
                    ], className='card-title'),
                    className='card-header'
                ),
                dbc.CardBody(
                    html.H4(id='grid-status', className='card-text')
                ),
            ], className='card mb-4 shadow'),
            width=4
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    html.H5([
                        html.I(className="fas fa-dollar-sign"),  # Icon for Realtime Marginal Pricing
                        html.Span(" Realtime Marginal Pricing", className='ml-2')
                    ], className='card-title'),
                    className='card-header'
                ),
                dbc.CardBody(
                    html.H4(id='marginal-pricing', className='card-text')
                ),
            ], className='card mb-4 shadow'),
            width=4
        ),
    ], className='mb-4'),
    dcc.Interval(
        id='update-interval',
        interval=40*1000,  # 40 seconds
        n_intervals=0
    )
], fluid=True)
