import dash_bootstrap_components as dbc
from dash import dcc

from datetime import date, timedelta


select_asset_layout = dbc.Row(
    [
        dbc.Label("Select an asset"),
        dcc.Dropdown(
            id="asset_id_select",
            options=[{"label": "BTC", "value": "bitcoin"}],
            value="bitcoin",
            className="mb-2",
        ),
    ]
)


date_picker_layout = dbc.Row(
    [
        dbc.Label("Date from / Date to"),
        dcc.DatePickerRange(
            id="date_picker",
            start_date=date.today() - timedelta(days=30),
            end_date=date.today(),
            start_date_placeholder_text="Start Period",
            end_date_placeholder_text="End Period",
            max_date_allowed=date.today(),
        ),
    ]
)


user_inputs_layout = dbc.Col(
    [dbc.Card([select_asset_layout, date_picker_layout], className="bg-light p-2")],
    width=4,
)


graph_layout = dbc.Col([dcc.Graph(id="asset_graph", className="border")], width=8)
