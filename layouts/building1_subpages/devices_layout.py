# layouts/building1_subpages/devices_layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc
from components.building_navbar import create_building_navbar  # Import the secondary navbar
import plotly.graph_objects as go
building1_navbar = create_building_navbar('GNIREBUILDING540')
import dash
import pandas as pd

# Sample data
data = {
    "Device ID": ["Device 1", "Device 2", "Device 3", "Device 4", "Device 5"],
    "Power Consumption (W)": [50, 75, 60, 45, 80],
    "Data RAM (GB)": [8, 16, 12, 4, 32],
    "Status": ["Active", "Inactive", "Active", "Maintenance", "Active"],
    "Priority": ["High", "Medium", "High", "Low", "Critical"],
}

df = pd.DataFrame(data)

# Create the table using Plotly's go.Table
table = go.Table(
    header=dict(
        values=list(df.columns),
        fill_color='lightgrey',
        align='center',
        font=dict(color='black', size=18, weight='bold'),
        height=40
    ),
    cells=dict(
        values=[df[col] for col in df.columns],
        align='center',
        font=dict(color='black', size=18, weight='bold'),
        height=40
    )
)



device_card = dbc.Card(
    [ dbc.CardHeader(
        html.H5([
            html.I(className="fas fa-sitemap", id="icon-ev"),
            html.Span(" Device info", className='ml-2')
        ], className='card-title'),
        className='card-header'
    ),
        dbc.CardBody(
            html.Div([
                dcc.Graph(
                            id='device-table',
                            figure={
                                'data': [table],
                                'layout': go.Layout(
                                    margin=dict(l=20, r=20, t=50, b=5),
                                    height=None,  # Allow it to expand naturally
                                    autosize=True,  # Enable autosizing
                                )
                            },config={'responsive': True},  # Make it responsive
                    style={'height': '100%', 'width': '100%'} 
                        )
            ], className='battery-container flex-row' , style={'width':'100%', 'padding': '0px', 'margin': '5px'})  # Add flex-row class for horizontal alignment
        ),
    ],
    className="mb-4 shadow  ", style={'padding': '0px', 'margin': '20px'},
)

data_store = dcc.Store(id='gnire-building-540-data-store')
devices_layout = html.Div([
    building1_navbar,
    data_store,
    html.H3("Building 1 - Devices Info"),
    # Add components specific to Devices Info
    # For example, a table or graphs showing device statuses
    html.Div(id='devices-content'),
    html.Div(device_card),
    
        # Include the Interval component if not already included
    dcc.Interval(
        id='nire-building-540-update-interval',
        interval=1*1000,  # Update every minute
        n_intervals=0
    ),
])
