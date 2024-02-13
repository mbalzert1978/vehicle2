import functools

from .settings.app import AppSettings
from .settings.base import AppEnvTypes, BaseAppSettings
from .settings.development import DevAppSettings
from .settings.production import ProdAppSettings
from .settings.test import TestAppSettings

environments: dict[AppEnvTypes, type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
    AppEnvTypes.test: TestAppSettings,
}


@functools.lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()  # type: ignore
