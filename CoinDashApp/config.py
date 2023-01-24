from typing import Optional
from pydantic import BaseSettings
from functools import lru_cache
import os


class Setting(BaseSettings):
    coin_api_token: Optional[str] = os.getenv(
        "COIN_API_TOKEN", None
    )


@lru_cache
def get_setting():
    return Setting()
