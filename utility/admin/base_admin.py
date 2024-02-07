from django.contrib.admin import ModelAdmin
from simple_history.admin import SimpleHistoryAdmin


class BaseAdmin(ModelAdmin):
    pass


class HistoryAdmin(BaseAdmin, SimpleHistoryAdmin):
    pass
