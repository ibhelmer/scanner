from django.contrib import admin
from .models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "mac_address", "ip_address")
    search_fields = ("name", "mac_address", "ip_address", "owner__username")
