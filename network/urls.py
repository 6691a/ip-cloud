from django.urls import path

from .views.whitelist import WhiteListListView

app_name = "network"

urlpatterns = [
    path("whitelist/", WhiteListListView.as_view(), name="whitelist_list"),
]
