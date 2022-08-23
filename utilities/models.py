from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampedModel


class Utility(models.Model):
    utility = models.CharField(max_length=25, unique=True)

    class Meta:
        verbose_name = _("Utility")
        verbose_name_plural = _("Utilities")

    def __str__(self):
        return self.utility


class Supplier(TimeStampedModel):
    supplier = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")

    def __str__(self):
        return self.supplier
