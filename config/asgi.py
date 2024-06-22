"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

DEPLOY_LEVEL = os.environ.get("DEPLOY_LEVEL", "development").lower()
MODULE = f"config.settings.{DEPLOY_LEVEL}"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", MODULE)

application = get_asgi_application()
