# dash imports
from dash import Dash, Input, Output
import dash_bootstrap_components as dbc

# modules imports
from coinapi_service import  get_asset_ids, get_asset_history
from layout import user_inputs_layout, graph_layout

# other imports
from datetime import date
import pandas as pd
import plotly.graph_objects as go
import time
import flask


server = flask.Flask(__name__) 

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, "style.css"],
    title="CoinDashApp",
    server=server # type: ignore
)


# LAYOUT

app.layout = dbc.Row(
    [
        user_inputs_layout,
        graph_layout,
    ],
    align="center",
    justify="center",
    className="h-100 w-100 bg-light",
    id="my-row",
)


# EXTRA FUNCTION


def str_date_to_unix_date(strdate: str):
    return int(time.mktime(date.fromisoformat(strdate).timetuple())) * 1000


# -- CALLBACKS -- #


@app.callback(Output("asset_id_select", "options"), Input("asset_id_select", "id"))
def get_assets_name_for_select(id: str):
    ids = get_asset_ids()
    return ids


@app.callback(
    Output("asset_graph", "figure"),
    Input("asset_id_select", "value"),
    Input("date_picker", "start_date"),
    Input("date_picker", "end_date"),
)
def show_graph_for_asset(asset_id: str, start_date: str, end_date: str):
    unix_start_date = str_date_to_unix_date(start_date)
    unix_end_date = str_date_to_unix_date(end_date)

    data = get_asset_history(asset_id, unix_start_date, unix_end_date)
    data = pd.DataFrame(data)
    data = data.astype({"priceUsd": "float"})

    fig = go.Figure(data=go.Bar(x=data["date"], y=data["priceUsd"]))
    fig.update_layout(xaxis_title="Date", yaxis_title="Price (USD)")
    fig.update_layout(
        title_text=f"{asset_id.capitalize()} price from {start_date} to {end_date}",
        font=dict(
            size=20,
        ),
        paper_bgcolor="#f8f9fa",
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=False)