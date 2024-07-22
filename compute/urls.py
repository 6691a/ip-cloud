from django.urls import include, path

app_name = "compute"

urlpatterns = [
    path("games/minecraft/", include("compute.minecraft.urls", namespace="minecraft")),
]
