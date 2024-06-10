from django.contrib import admin

from utility.admin import HistoryAdmin

from .models import Accounts


@admin.register(Accounts)
class AccountsAdmin(HistoryAdmin):
    site_header = "Accounts Admin"
