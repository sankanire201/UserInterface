
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import pandas as pd
import random
from components.building_navbar import create_building_navbar  # Import the secondary navbar
import plotly.graph_objects as go

#place holder for battery information table

battery_status_table =  go.Figure(data=[go.Table(
  header = dict(
    values = [['<b>Inv buy</b>'],['<b>Inv sell</b>'],['<b>Inv load</b>'],['<b>Inv out</b>'],['<b>Batt SOC</b>'],['<b>Batt Volt</b>']],
    line_color='darkslategray',
    fill_color='royalblue',
    align=['left','center'],
    font=dict(color='white', size=12),
  ),
  cells=dict(
    values=[str(10)+'kW',str(10)+'kW',str(10)+'kW',str(10)+'kW',str(10)+'%',str(220)+'V'],
    line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    fill_color='white',
    align=['center', 'center'],
    font=dict(color='black', size=14,weight='bold'),
    height=30)
    )
])

battery_status_table.update_layout(
    autosize=True,
    height=80,
    margin=dict(l=5, r=5, t=5, b=5),  # Remove extra margins
)
#place holder for the bar chart

data = {
    'Building': ['group 0', 'group 1','group 2', 'group 3','generation', 'Total controllabe'],
    'Consumption': [6000, 10000,6000, 10000,6000, 10000]
}
df = pd.DataFrame(data)
df['Text'] = df['Building'] + ': ' + df['Consumption'].astype(str) + ' kW'

color_discrete_map = {
    'Building 1': '#1f77b4',
    'Building 2': '#ff7f0e',
}

bar_fig = px.bar(
    df,
    x='Consumption',
    y='Building',
    orientation='h',
    text='Text',
    color='Building',
    color_discrete_map=color_discrete_map
)

bar_fig.update_traces(
    textposition='inside',
    textfont=dict(color='white', size=12),
    insidetextanchor='end'
)

bar_fig.update_layout(
    showlegend=False,
    margin=dict(l=0, r=0, t=0, b=0),
    xaxis_title='Consumption (kW)',
    yaxis_title='',
)




# Placeholder data for the pie chart
consumption_data = {
    'Load Group': ['Lighting', 'HVAC', 'Equipment'],
    'Consumption': [40, 35, 25]  # Percentages
}
consumption_df = pd.DataFrame(consumption_data)

# Create the pie chart
consumption_pie_fig = px.pie(
    consumption_df,
    names='Load Group',
    values='Consumption',
    color='Load Group',
    color_discrete_map={
        'Lighting': '#1f77b4',
        'HVAC': '#ff7f0e',
        'Equipment': '#2ca02c'
    },
    hole=0.4  # For a donut chart effect
)

consumption_pie_fig.update_layout(
    showlegend=True,
    legend_title_text='Load Groups',
    margin=dict(l=0, r=0, t=0, b=0),
)



# layouts/building1_layout.py

import dash_bootstrap_components as dbc
from dash import html, dcc

# ... other imports and code ...

# layouts/building1_layout.py

import dash_bootstrap_components as dbc
from dash import html, dcc
from app_instance import app  # Ensure app is imported if using app.get_asset_url()


import pandas as pd
import plotly.express as px

# Sample data for energy consumption over time
consumption_time_data = pd.DataFrame({
    'Timestamp': pd.date_range(start='2021-01-01', periods=24, freq='H'),
    'Consumption': [random.uniform(50, 150) for _ in range(24)]
})

# Create the line chart
consumption_time_fig = px.line(
    consumption_time_data,
    x='Timestamp',
    y='Consumption',
    title='Energy Consumption Over Time',
    labels={'Timestamp': 'Time', 'Consumption': 'Consumption (kWh)'}
)

consumption_time_fig.update_layout(
    margin=dict(l=20, r=20, t=50, b=20),
    paper_bgcolor='white',
    plot_bgcolor='white',
    hovermode='x unified'
)

consumption_time_fig.update_xaxes(
    showgrid=True,   # Show x-axis grid lines
    gridwidth=1,     # Width of x-axis grid lines
    gridcolor='LightGray'  # Color of x-axis grid lines
)
consumption_time_fig.update_yaxes(
    showgrid=True,   # Show y-axis grid lines
    gridwidth=1,     # Width of y-axis grid lines
    gridcolor='LightGray'  # Color of y-axis grid lines
)

# Sample data for energy production vs. consumption
production_consumption_data = pd.DataFrame({
    'Type': ['Production', 'Consumption'],
    'Energy': [random.uniform(1000, 1500), random.uniform(1200, 1700)]
})

# Create the bar chart
production_consumption_fig = px.bar(
    production_consumption_data,
    x='Type',
    y='Energy',
    color='Type',
    title='Energy Production vs. Consumption',
    labels={'Energy': 'Energy (kWh)'},
    color_discrete_map={'Production': '#1f77b4', 'Consumption': '#ff7f0e'}
)

production_consumption_fig.update_layout(
    margin=dict(l=20, r=20, t=50, b=20),
    paper_bgcolor='white',
    plot_bgcolor='white',
    showlegend=False
)

# Energy Consumption Over Time Card
energy_generation_card = dbc.Card([
    dbc.CardHeader(
        html.H5("Energy Generation Over Time", className='card-title'),
        className='card-header'
    ),
    dbc.CardBody(
        dcc.Graph(
            id='generation-time-chart',
            figure=consumption_time_fig
        )
    ),
], className='card mb-4 shadow')



# Energy Consumption Over Time Card
lmp_time_card = dbc.Card([
    dbc.CardHeader(
        html.H5("LMP Over Time", className='card-title'),
        className='card-header'
    ),
    dbc.CardBody(
        dcc.Graph(
            id='lmp-time-chart',
            figure=consumption_time_fig
        )
    ),
], className='card mb-4 shadow')







# Energy Consumption Over Time Card
consumption_time_card = dbc.Card([
    dbc.CardHeader(
        html.H5("Energy Consumption Over Time", className='card-title'),
        className='card-header'
    ),
    dbc.CardBody(
        dcc.Graph(
            id='consumption-time-chart',
            figure=consumption_time_fig
        )
    ),
], className='card mb-4 shadow')


# Energy Production vs. Consumption Card
production_consumption_card = dbc.Card([
    dbc.CardHeader(
        html.H5("priority Group Consumption", className='card-title'),
        className='card-header'
    ),
    dbc.CardBody(
        dcc.Graph(
            id='production-consumption-chart',
            figure=production_consumption_fig
        )
    ),
], className='card mb-4 shadow')






# EV Card using Flexbox Layout
ev_card = dbc.Card([
    dbc.CardHeader(
        html.H5([
            html.I(className="fas fa-car", id="icon-ev"),
            html.Span(" Electric Vehicle", className='ml-2')
        ], className='card-title'),
        className='card-header'
    ),
    dbc.CardBody(
        html.Div([
            # EV Image
            html.Img(
                src=app.get_asset_url('ev_image.jpg'),
                id='ev-image',
                className='ev-image'
            ),
            # EV Status with Icon using Flexbox
            html.Div([
                html.I(id='ev-status-icon'),
                html.Span(id='building1-ev-status')
            ], className='ev-status-flex'),
            # EV Battery Level
            html.P(id='building1-ev-battery-level', className='card-text'),
        ], className='min-height-ev-card ev-container'),
    ),
], className= 'mb-4 shadow')

            # html.P(id='building1-battery-SOC', className='card-text'),
            # html.P(id='building1-battery-voltage', className='card-text'),
            # html.P(id='building1-battery-inv-load', className='card-text'),
            # html.P(id='building1-battery-inv-buy', className='card-text'),
            # html.P(id='building1-battery-inv-sell', className='card-text'),
            # html.P(id='building1-battery-cc-watt', className='card-text'),
# Define the first inner card with Flexbox to display text horizontally
battery_inner_card_1 = dbc.Card(
    [
        dbc.CardBody(
             html.Div(dcc.Graph(id='building1-battery-status-table', figure=battery_status_table)),className='battery-container flex-row', style={'width': '100%', 'padding': '0px', 'margin-left': '0px'},  # Add flex-row class for horizontal alignment
        )
    ],
    className="mb-4 shadow", style={'width': '100%', 'padding': '0px', 'margin': '0px'},
)

# Define the second inner card with Flexbox to display text horizontally
battery_inner_card_2 = dbc.Card(
    [
        dbc.CardBody(
            html.Div([
                html.H5(id='building1-battery-SOC', className='small-text'),
                html.H5(id='building1-battery-voltage', className='small-text'),
            ], className='battery-container flex-row' , style={'width': '100%', 'padding': '0px', 'margin': '0px'})  # Add flex-row class for horizontal alignment
        ),
    ],
    className="mb-4 shadow  ", style={'width': '100%', 'padding': '0px', 'margin': '0px'},
)


# Battery Information Card
battery_card = dbc.Card([
    dbc.CardHeader(
        html.H5([
            html.I(className="fas fa-battery-full", id="icon-ev"),
            html.Span(" Battery", className='ml-2')
        ], className='card-title'),
        className='card-header'
    ),
    dbc.CardBody(
        html.Div([
            # EV Image
            html.Img(
                src=app.get_asset_url('battery.jpg'),
                id='ev-image',
                className='battery-image'
            ),
            # EV Status with Icon using Flexbox
            html.Div([
                html.I(id='battery-status-icon'),
                html.Span(id='building1-battery-status'),
                                html.Div(
                    battery_inner_card_1, 
                    style={'width': '100%', 'padding': '0', 'margin': '0'}
                ),  #
            ], className='battery-status-flex' , style={'width': '100%', 'padding': '0','margin': '0'}),
            # EV Battery Level
              

        ], className='ev-container', style={'width': '100%', 'padding': '0','margin': '0'}),
    ),
], className='card mb-4 shadow',  style={'width': '100%', 'padding': '0', 'margin': '0'})


# Pricing Information Card
pricing_card = dbc.Card([
    dbc.CardHeader(
        html.H5([
            html.I(className="fas fa-dollar-sign", id="icon-pricing"),
            html.Span(" Pricing Information", className='ml-2')
        ], className='card-title'),
        className='card-header'
    ),
    dbc.CardBody([
        # Real-time Marginal Price
        html.Div([
            html.Span("Real-time Marginal Price: ", className='pricing-label'),
            html.Span(id='building1-realtime-marginal-price', className='pricing-value'),
            html.Span(id='building1-realtime-marginal-trend', className='pricing-trend ml-2'),
        ], className='mb-2'),
        # Hourly Price
        html.Div([
            html.Span("Hourly Price: ", className='pricing-label'),
            html.Span(id='building1-hourly-price', className='pricing-value'),
            html.Span(id='building1-hourly-price-trend', className='pricing-trend ml-2'),
        ], className='mb-2'),
        # Hourly Cost
        html.Div([
            html.Span("Hourly Cost: ", className='pricing-label'),
            html.Span(id='building1-hourly-cost', className='pricing-value'),
            html.Span(id='building1-hourly-cost-trend', className='pricing-trend ml-2'),
        ]),
    ]),
], className='card mb-4 shadow')


# Consumption Information Card
consumption_card = dbc.Card([
    dbc.CardHeader(
        html.H5([
            html.I(className="fas fa-chart-pie", id="icon-consumption"),
            html.Span(" Consumption and Generation Information", className='ml-2')
        ], className='card-title'),
        className='card-header'
    ),
    dbc.CardBody(
        dcc.Graph(id='building1-consumption-bar', figure=bar_fig)
    ),
], className='card mb-4 shadow')

# Create the secondary navigation bar
building1_navbar = create_building_navbar('building1')
# Include a dcc.Store component
data_store = dcc.Store(id='building1-data-store')
building1_layout = dbc.Container([
    html.Div(style={'height': '30px'}),  # Spacer
    # Include the secondary navigation bar
    building1_navbar,
    data_store,
    # Row with the three existing cards
    dbc.Row([
        dbc.Col(
            ev_card,
            width=4
        ),
        dbc.Col([
        dbc.Col(
            pricing_card,
            width=14,
        ),
        dbc.Col(
            battery_card,
            width=14
        )        
        ]),
        dbc.Col(
            consumption_card,
            width=4
        ),
    ], className='mb-4'),

    # Row with the two new chart cards
    dbc.Row([
        dbc.Col(
            consumption_time_card,
            width=6
        ),
        dbc.Col(
            production_consumption_card,
            width=6
        ),
    ], className='mb-4'),
    
   # Row with the two new chart cards
    dbc.Row([
        dbc.Col(
            energy_generation_card,
            width=6
        ),
        dbc.Col(
            lmp_time_card,
            width=6
        ),
    ], className='mb-4'),
    # Include the Interval component if not already included
    dcc.Interval(
        id='building1-update-interval',
        interval=10*1000,  # Update every minute
        n_intervals=0
    ),
], fluid=True)