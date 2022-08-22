from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from account_managers.models import AccountManager
from client_managers.models import ClientManager

from .models import Client


class ClientResource(resources.ModelResource):

    account_manager = fields.Field(
        column_name="account_manager",
        attribute="account_manager",
        widget=ForeignKeyWidget(AccountManager, field="account_manager__name"),
    )

    client_manager = fields.Field(
        column_name="client_manager",
        attribute="client_manager",
        widget=ManyToManyWidget(ClientManager, field="client_manager", separator=","),
    )

    class Meta:
        model = Client
        skip_unchanged = True
        report_skipped = True
        fields = [
            "id",
            "client_name",
            "account_manager",
            "client_manager",
        ]
        import_id_fields = ["id"]

        export_order = [
            "client_name",
            "account_manager",
            "client_manager",
        ]


class ClientAdmin(ImportExportModelAdmin):
    show_full_result_count = False
    resource_class = ClientResource
    list_display = ("client_name", "account_manager", "client_managers")
    autocomplete_fields = ("account_manager", "client_manager")
    search_fields = ("client_name",)
    list_per_page = 25
    search_help_text = "Search by Client Name"

    def client_managers(self, instance):
        return [client_manager for client_manager in instance.client_manager.all()[:3]]


admin.site.register(Client, ClientAdmin)
