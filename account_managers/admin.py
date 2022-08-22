from django.contrib import admin
from django.contrib.auth import get_user_model
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

from .models import AccountManager

User = get_user_model()


class AMResource(resources.ModelResource):

    account_manager = fields.Field(
        column_name="account_manager",
        attribute="account_manager",
        widget=ForeignKeyWidget(
            User,
            field="email",
        ),
    )

    class Meta:
        model = AccountManager
        skip_unchanged = True
        report_skipped = True
        fields = ["account_manager", "id", "account_manager__name"]
        import_id_fields = [
            "id",
        ]


class AccountManagerAdmin(ImportExportModelAdmin):
    resource_class = AMResource
    list_display = ("account_manager", "get_account_manager_name", "id")
    search_fields = ("account_manager__name",)

    def get_account_manager_name(self, obj):
        return obj.account_manager.name

    get_account_manager_name.short_description = "Name"


admin.site.register(AccountManager, AccountManagerAdmin)
