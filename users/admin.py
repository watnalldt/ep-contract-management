from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin

from .models import CustomUser


class UserResource(resources.ModelResource):
    class Meta:
        model = CustomUser
        skip_unchanged = True
        report_skipped = True
        exclude = ["first_name", "last_name"]
        import_id_fields = ["email"]


class CustomUserAdmin(BaseUserAdmin, ImportExportModelAdmin):
    resource_class = UserResource
    fieldsets = (
        (None, {"fields": ("name", "email", "password", "last_login")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_client_manager",
                    "is_account_manager",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "email", "password1", "password2"),
            },
        ),
    )

    list_display = (
        "name",
        "email",
        "is_staff",
        "is_account_manager",
        "is_client_manager",
        "last_login",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "is_account_manager",
        "is_client_manager",
        "groups",
    )
    search_fields = (
        "email",
        "name",
    )
    search_help_text = "Enter name or email"
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(CustomUser, CustomUserAdmin)
