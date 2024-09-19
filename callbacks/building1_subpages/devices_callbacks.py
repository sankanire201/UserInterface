# callbacks/building1_subpages/devices_callbacks.py

from dash import Input, Output, State
from app_instance import app

# Example callback for updating devices content
@app.callback(
    Output('devices-content', 'children'),
    Input('building1-update-interval', 'n_intervals')
)
def update_devices_content(n):
    # Implement logic to update devices information
    return html.Div([
        html.P(f"Devices info updated at interval {n}")
    ])
