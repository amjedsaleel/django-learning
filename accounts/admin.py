from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Account

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin')


admin.site.register(Account)