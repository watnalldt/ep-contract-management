from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

from clients.models import Client
from utilities.models import Supplier, Utility

from .models import Contract


class ContractResource(resources.ModelResource):

    client_name = fields.Field(
        column_name="client_name",
        attribute="client_name",
        widget=ForeignKeyWidget(Client, "client_name"),
    )

    supplier = fields.Field(
        column_name="supplier",
        attribute="supplier",
        widget=ForeignKeyWidget(Supplier, "supplier"),
    )

    utility = fields.Field(
        column_name="utility",
        attribute="utility",
        widget=ForeignKeyWidget(Utility, "utility"),
    )

    class Meta:
        model = Contract
        skip_unchanged = True
        report_skipped = True
        # exclude = ("id",)
        import_id_fields = ("mpan_mpr",)


# class ClientFilter(AutocompleteFilter):
#     title = "Client"  # display title
#     field_name = "client_name"  # name of the foreign key field
#
#
# class SupplierFilter(AutocompleteFilter):
#     title = "Supplier"  # display title
#     field_name = "supplier"  # name of the foreign key field
#
#
# class FuelTypeFilter(AutocompleteFilter):
#     title = "Fuel Type"  # display title
#     field_name = "fuel_type"  # name of the foreign key field


def make_out_of_contract(modeladmin, request, queryset):
    queryset.update(is_ooc="True")


make_out_of_contract.short_description = "Mark selected contracts out of contract"


def make_in_contract(modeladmin, request, queryset):
    queryset.update(is_ooc="False")


make_in_contract.short_description = "Mark selected contracts in contract"


def needs_directors_approval(modeladmin, request, queryset):
    queryset.update(is_directors_approval="True")


needs_directors_approval.short_description = (
    "Mark selected contracts for Directors Approval"
)


def directors_approval_removed(modeladmin, request, queryset):
    queryset.update(is_directors_approval="False")


directors_approval_removed.short_description = (
    "Mark selected contracts for Directors Approval Removed"
)


class ContractAdmin(ImportExportModelAdmin):
    show_full_result_count = False
    resource_class = ContractResource
    list_per_page = 25
    list_display = (
        "site_name",
        "client_name",
        "site_address",
        "supplier",
        "utility",
        "meter_serial_number",
        "mpan_mpr",
        "eac",
        "contract_end_date",
        "is_ooc",
        "is_directors_approval",
        "vat",
    )

    def get_rangefilter_contract_end_date_title(self, request, field_path):
        return "Contract End Date"

    list_filter = [
        # ClientFilter,
        # SupplierFilter,
        # FuelTypeFilter,
        # ("contract_end_date", DateRangeFilter),
        "is_ooc",
        "is_directors_approval",
    ]
    search_help_text = (
        "Search by MPAN/MPR or Site Name/ClientName, Site Address or Meter Serial No."
    )
    search_fields = (
        "site_name",
        "client_name__client_name",
        "mpan_mpr",
        "contract_end_date",
        "meter_serial_number",
        "site_address",
    )
    ordering = ["-contract_end_date"]
    date_hierarchy = "contract_end_date"
    actions = [
        make_out_of_contract,
        make_in_contract,
        needs_directors_approval,
        directors_approval_removed,
    ]


admin.site.register(Contract, ContractAdmin)
