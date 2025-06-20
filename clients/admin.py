from django.contrib import admin
from .models import APPClient

# Register your models here.

class APPClientAdmin(admin.ModelAdmin):
    readonly_fields = ('client_id', 'client_secret', 'created_at')
    list_display = ('client_name', 'client_id', 'created_at')
    search_fields = ('client_name', )

admin.site.register(APPClient, APPClientAdmin)
