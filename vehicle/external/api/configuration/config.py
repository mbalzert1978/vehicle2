import functools

from vehicle.external.api.configuration.settings.app import AppSettings
from vehicle.external.api.configuration.settings.base import AppEnvTypes, BaseAppSettings
from vehicle.external.api.configuration.settings.development import DevAppSettings
from vehicle.external.api.configuration.settings.production import ProdAppSettings
from vehicle.external.api.configuration.settings.test import TestAppSettings

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
