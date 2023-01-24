from typing import Optional
from pydantic import BaseSettings
from functools import lru_cache
import os


class Setting(BaseSettings):
    coin_api_token: Optional[str] = os.getenv(
        "COIN_API_TOKEN", "ebe1bd1e-7ae7-4af0-81d0-d2479e40a1fd"
    )


@lru_cache
def get_setting():
    return Setting()
