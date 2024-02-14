import logging

from pydantic_settings import SettingsConfigDict

from ..settings.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "Dev FastAPI Vehicle"

    logging_level: int = logging.DEBUG
    model_config = SettingsConfigDict(env_file=".env")
