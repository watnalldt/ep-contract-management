from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from clients.models import Client
from core.models import TimeStampedModel
from utilities.models import Supplier, Utility


class ContractsManager(models.Manager):
    def get_queryset(self):
        return (
            super(ContractsManager, self)
            .get_queryset()
            .select_related("client_name", "supplier", "utility")
        )


class Contract(TimeStampedModel):

    client_name = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="client_contracts"
    )
    # TODO: "check on_delete"
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name="contract_suppliers"
    )
    # TODO: "check on_delete"
    utility = models.ForeignKey(
        Utility, on_delete=models.CASCADE, related_name="contract_utilities"
    )
    # TODO: "check on_delete"
    account_number = models.CharField(max_length=30, null=True, blank=True)
    company_reg_number = models.CharField(max_length=20, null=True, blank=True)
    site_name = models.CharField(max_length=255)
    site_address = models.CharField(max_length=255)
    meter_serial_number = models.CharField(max_length=30, null=True, blank=True)
    top_line = models.CharField(max_length=30)
    mpan_mpr = models.CharField(max_length=255)
    contract_end_date = models.DateField(null=True, blank=True)
    is_ooc = models.BooleanField(default=False)
    is_directors_approval = models.BooleanField(default=False)
    eac = models.CharField(max_length=30)
    vat = models.CharField(max_length=10, null=True, blank=True)
    smart_meter = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        indexes = [
            models.Index(fields=["mpan_mpr"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["mpan_mpr", "contract_end_date"],
                name="unique_contract",
            )
        ]
        verbose_name = _("Client Contract")
        verbose_name_plural = _("Client Contracts")
        ordering = ["contract_end_date"]

    objects = ContractsManager()

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this client."""
        return reverse("contracts:contract_detail", args=[str(self.pk)])
