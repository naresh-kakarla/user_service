from django.contrib import admin
from .models import UserAccount

# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display= ('username', 'first_name', 'last_name')
    search_fields = ('username', 'email')

admin.site.register(UserAccount, UserAccountAdmin)

admin.site.site_header = "E-Service"
admin.site.site_title = "My E-Service Portal"
admin.site.index_title = "Welcome to Admin Dashboard"

