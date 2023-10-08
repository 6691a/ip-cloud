import sentry_sdk
from google.oauth2 import service_account
from sentry_sdk.integrations.django import DjangoIntegration

from .settings import *

INSTALLED_APPS += []

MIDDLEWARE += []

sentry_sdk.init(
    dsn=cfg["SENTRY_DNS"],
    integrations=[DjangoIntegration()],
    send_default_pii=True,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

CREDENTIALS = service_account.Credentials.from_service_account_file(
    BASE_DIR / cfg["GCP_CREDENTIAL"]
)
STORAGES = cfg["STORAGES"]
STORAGES["default"]["OPTIONS"]["credentials"] = CREDENTIALS
STORAGES["staticfiles"]["OPTIONS"]["credentials"] = CREDENTIALS
