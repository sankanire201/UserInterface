# callbacks/building1_subpages/devices_callbacks.py

from dash import Input, Output, State, html
from app_instance import app

# Example callback for updating devices content
@app.callback(
    Output('gnire-building-540-data-store', 'data'),
    Input('nire-building-540-update-interval', 'n_intervals')
)
def update_devices_content(n):
    data={
        'data': n
    }
    # Implement logic to update devices information
    return data

@app.callback(
    Output('devices-content','children'),
    Input('gnire-building-540-data-store', 'data')
)
def query_database(data):
    
    return data.get('data',0)