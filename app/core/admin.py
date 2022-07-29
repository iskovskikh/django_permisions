from django.contrib import admin

# Register your models here.
from core.models import Settings


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass
