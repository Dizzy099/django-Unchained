from django.contrib import admin
from .models import Visit


@admin.register(Visit)
class VisitsAdmin(admin.ModelAdmin):
    pass
