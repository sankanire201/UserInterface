# callbacks/home_callbacks.py
from dash import Input, Output, html
import plotly.express as px
import pandas as pd
import numpy as np
import random
import datetime
# callbacks/home_callbacks.py

from dash import Input, Output, State, html
from app_instance import app
import random

# @app.callback(
#     Output('output', 'children'),
#     Input('update-interval', 'n_intervals')  # Corrected ID
# )
# def update_output(n):
#     print(f"Callback triggered at n_intervals={n}")
#     return f"Interval has triggered {n} times."

prev_realtime_price = [None]
prev_hourly_price = [None]
prev_hourly_cost = [None]

status_class_map = {
    ' Normal': 'grid-status-normal',
    ' Warning': 'grid-status-warning',
    ' Critical': 'grid-status-critical'
}

# Define grid statuses and their corresponding styles and icons
GRID_STATUSES = {
    'Normal': {
        'color': 'green',
        'icon_class': 'fas fa-check-circle'
    },
    'Warning': {
        'color': 'orange',
        'icon_class': 'fas fa-exclamation-triangle'
    },
    'Critical': {
        'color': 'red',
        'icon_class': 'fas fa-times-circle'
    }
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
    df = pd.DataFrame(data)
    
    # Create a 'Text' column with the building name and consumption
    df['Text'] = df['Building'] + ': ' + df['Consumption'].astype(str) + ' kW'
    
    # Define a color mapping for each building
    color_discrete_map = {
        'Building 1': '#1f77b4',  # Blue
        'Building 2': '#ff7f0e',  # Orange
    }
    
    # Create the bar chart
    fig = px.bar(
        df,
        x='Consumption',
        y='Building',
        orientation='h',
        text='Text',
        color='Building',
        color_discrete_map=color_discrete_map
    )
    
    # Update the text position and styling
    fig.update_traces(
        textposition='inside',
        textfont=dict(color='white', size=12),
        insidetextanchor='end'
    )
    
    # Remove the legend (optional)
    fig.update_layout(
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis_title='Consumption (kW)',
        yaxis_title='',
    )
    
    return fig

@app.callback(
    [Output('grid-status', 'children'),
     
     Output('grid-status-icon', 'className'),
     Output('grid-status-icon', 'style')],
    Input('update-interval', 'n_intervals')
)
def update_grid_status(n):
    grid_status = random.choice(['Normal', 'Warning', 'Critical'])

    # Get the styles and icon based on the grid status
    status_info = GRID_STATUSES[grid_status]
    color = status_info['color']
    icon_class = status_info['icon_class']

    # Return the status text, style, icon class, and icon style
    return (grid_status,
            icon_class,
            {'color': color, 'font-size': '2em', 'display': 'inline-block', 'vertical-align': 'middle'})


@app.callback(
    Output('total-power-chart', 'figure'),
    Input('update-interval', 'n_intervals')
)
def update_total_power_chart(n):
    # Simulated data
    now = datetime.datetime.now()
    time_index = [now - datetime.timedelta(hours=i) for i in reversed(range(24))]
    total_power_data = [random.randint(100, 200) for _ in range(24)]

    total_power_df = pd.DataFrame({
        'Time': time_index,
        'Total Power': total_power_data
    })

    fig = px.line(total_power_df, x='Time', y='Total Power', title='Total Power Consumption')
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    return fig

@app.callback(
    Output('priority-power-chart', 'figure'),
    Input('update-interval', 'n_intervals')
)
def update_priority_power_chart(n):
    # Simulated data
    now = datetime.datetime.now()
    time_index = [now - datetime.timedelta(hours=i) for i in reversed(range(24))]
    priority_power_data = [random.randint(50, 100) for _ in range(24)]

    priority_power_df = pd.DataFrame({
        'Time': time_index,
        'Priority Power': priority_power_data
    })

    fig = px.line(priority_power_df, x='Time', y='Priority Power', title='Priority Group Power Consumption')
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    return fig


@app.callback(
    Output('realtime-marginal-price', 'children'),
    Output('realtime-marginal-trend', 'children'),
    Input('update-interval', 'n_intervals')
)
def update_realtime_marginal_price(n):
    # Simulated real-time marginal price
    price = round(random.uniform(50, 150), 2)
    # Determine trend
    trend = ''
    if prev_realtime_price[0] is not None:
        if price > prev_realtime_price[0]:
             trend = html.Span(' ▲', style={'color': 'green'})
        elif price < prev_realtime_price[0]:
            trend = html.Span('▼', style={'color': 'red'})
    # Update previous value
    prev_realtime_price[0] = price
    return f"${price}/MWh", trend

@app.callback(
    Output('hourly-price', 'children'),
    Output('hourly-price-trend', 'children'),
    Input('update-interval', 'n_intervals')
)
def update_hourly_price(n):
    # Simulated hourly price
    price = round(random.uniform(40, 160), 2)
    # Determine trend
    trend = ''
    if prev_hourly_price[0] is not None:
        if price > prev_hourly_price[0]:
             trend = html.Span(' ▲', style={'color': 'green'})
        elif price < prev_hourly_price[0]:
            trend = html.Span('▼', style={'color': 'red'})
    # Update previous value
    prev_hourly_price[0] = price
    return f"${price}/MWh", trend

@app.callback(
    Output('hourly-cost', 'children'),
    Output('hourly-cost-trend', 'children'),
    Input('update-interval', 'n_intervals')
)
def update_hourly_cost(n):
    # Simulated hourly cost
    cost = round(random.uniform(5000, 10000), 2)
    # Determine trend
    trend = ''
    if prev_hourly_cost[0] is not None:
        if cost > prev_hourly_cost[0]:
             trend = html.Span(' ▲', style={'color': 'green'})
        elif cost < prev_hourly_cost[0]:
            trend = html.Span('▼', style={'color': 'red'})
    # Update previous value
    prev_hourly_cost[0] = cost
    return f"${cost}", trend