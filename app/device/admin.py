from django.contrib import admin
from .models import Department, Device

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']

admin.site.register(Department)
admin.site.register(Device, DeviceAdmin)
