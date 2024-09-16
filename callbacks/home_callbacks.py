# callbacks/home_callbacks.py
from dash import Input, Output, html
import plotly.express as px
from app import app
import random

status_class_map = {
    'Normal': 'grid-status-normal',
    'Warning': 'grid-status-warning',
    'Critical': 'grid-status-critical'
}

@app.callback(
    Output('consumption-chart', 'figure'),
    Input('update-interval', 'n_intervals')
)
def update_consumption_chart(n):
    # Simulated data
    data = {
        'Building': ['Building 1', 'Building 2'],
        'Consumption': [random.randint(80, 120), random.randint(130, 170)]
    }
    fig = px.bar(data, x='Consumption', y='Building', orientation='h')
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

@app.callback(
    Output('grid-status', 'children'),
    Input('update-interval', 'n_intervals')
)
def update_grid_status(n):
    status = random.choice(['Normal', 'Warning', 'Critical'])
    status_class = status_class_map[status]
    return html.Span(status, className=status_class)

@app.callback(
    Output('marginal-pricing', 'children'),
    Input('update-interval', 'n_intervals')
)
def update_marginal_pricing(n):
    price = round(random.uniform(50, 150), 2)
    return f"${price}/MWh"
