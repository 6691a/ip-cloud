from os import environ

from celery import Celery
from kombu import Exchange, Queue

DEPLOY_LEVEL = environ.get("DEPLOY_LEVEL", "development").lower()
MODULE = f"config.settings.{DEPLOY_LEVEL}"
environ.setdefault("DJANGO_SETTINGS_MODULE", MODULE)

app = Celery("playhub")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

# 작업 큐 설정
app.conf.task_default_queue = "default"
app.conf.task_queues = [
    Queue("default", Exchange("default"), routing_key="default"),
    Queue("notification", Exchange("notification"), routing_key="noti.#"),
]

# app.conf.beat_schedule = {}
