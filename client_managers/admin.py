from django.contrib import admin

from .models import ClientManager


class ClientManagerAdmin(admin.ModelAdmin):
    list_display = ("client_manager",)
    search_fields = ("client_manager__email",)


admin.site.register(ClientManager, ClientManagerAdmin)
