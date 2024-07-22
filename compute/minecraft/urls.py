from django.urls import path

from .views import HomeView

app_name = "minecraft"

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
]
