import sentry_sdk
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
