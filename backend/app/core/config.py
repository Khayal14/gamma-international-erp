from pydantic_settings import BaseSettings, EnvSettingsSource, SettingsConfigDict
from typing import List, Any, Tuple, Type
import json


class CORSAwareEnvSource(EnvSettingsSource):
    """
    Custom env source that pre-processes ALLOWED_ORIGINS before pydantic-settings
    calls json.loads() on it.  Handles three formats:
      - empty string   → use field default
      - JSON array     → ["https://a.com","http://localhost:3000"]
      - comma list     → https://a.com,http://localhost:3000
      - single URL     → https://a.com
    """

    def prepare_field_value(
        self, field_name: str, field: Any, value: Any, value_is_complex: bool
    ) -> Any:
        if field_name == "ALLOWED_ORIGINS" and isinstance(value, str):
            value = value.strip()
            if not value:
                return None  # falls back to field default
            if not value.startswith("["):
                # Convert to JSON array so the parent can json.loads() it
                origins = [o.strip() for o in value.split(",") if o.strip()]
                value = json.dumps(origins)
        return super().prepare_field_value(field_name, field, value, value_is_complex)


class Settings(BaseSettings):
    # App
    APP_NAME: str = "Gamma International ERP"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "production"

    # Database
    DATABASE_URL: str

    # Redis
    REDIS_URL: str = "redis://localhost:6379"

    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    # MinIO / S3
    MINIO_ENDPOINT: str = ""
    MINIO_ACCESS_KEY: str = ""
    MINIO_SECRET_KEY: str = ""
    MINIO_BUCKET: str = "gamma-erp"
    MINIO_USE_SSL: bool = True

    # CORS — accepts JSON array, comma-separated URLs, single URL, or empty (→ default)
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        env_ignore_empty=True,  # empty env vars fall back to field defaults
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: Any,
        env_settings: Any,
        dotenv_settings: Any,
        file_secret_settings: Any,
    ) -> Tuple[Any, ...]:
        return (
            init_settings,
            CORSAwareEnvSource(settings_cls),
            dotenv_settings,
            file_secret_settings,
        )


settings = Settings()
