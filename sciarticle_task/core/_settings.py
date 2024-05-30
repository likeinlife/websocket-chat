from functools import partial

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

_model_config = partial(SettingsConfigDict, env_file=".env", extra="ignore")


class RabbitSettings(BaseSettings):
    model_config = _model_config(env_prefix="RABBIT_")

    title: str = Field(init=False)
    version: str = Field(init=False)
    debug: bool = Field(init=False)


class LoggingSettings(BaseSettings):
    model_config = _model_config(env_prefix="LOGGING_")

    level: str = Field(default="INFO", init=False)
    json_format: bool = Field(default=False, init=False)


class AppSettings(BaseSettings):
    model_config = _model_config(env_prefix="APP_")

    name: str = Field(init=False)


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    logging: LoggingSettings = LoggingSettings()
    rabbit: RabbitSettings = RabbitSettings()


settings = Settings()
