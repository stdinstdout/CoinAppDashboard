from config import get_setting

from http import client
import json


class BadResponseException(Exception):
    pass


def get_asset_ids():
    conn = client.HTTPSConnection("api.coincap.io")

    token = get_setting().coin_api_token
    if token:
        headers = {"Authorization": f"Bearer {get_setting().coin_api_token}"}
    else:
        headers = {}

    payload = ""
    conn.request("GET", "/v2/assets/", payload, headers)
    res = conn.getresponse()

    if res.status != 200:
        raise BadResponseException("Bad response")

    data = json.loads(res.read())  # type: ignore
    return [{"label": row["symbol"], "value": row["id"]} for row in data["data"]]


def get_asset_history(asset_id: str, start_date: int, end_date: int):
    conn = client.HTTPSConnection("api.coincap.io")

    token = get_setting().coin_api_token
    if token:
        headers = {"Authorization": f"Bearer {get_setting().coin_api_token}"}
    else:
        headers = {}

    payload = ""
    interval = "d1"

    conn.request(
        "GET",
        f"/v2/assets/{asset_id}/history?interval={interval}&start={start_date}&end={end_date}",
        payload,
        headers,
    )
    res = conn.getresponse()

    if res.status != 200:
        raise BadResponseException("Bad response")

    data = json.loads(res.read())  # type: ignore
    return data["data"]
