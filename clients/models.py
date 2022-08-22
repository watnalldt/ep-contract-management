from django.db import models
from django.urls import reverse

from account_managers.models import AccountManager
from client_managers.models import ClientManager
from core.models import TimeStampedModel


class ClientsManager(models.Manager):
    def get_queryset(self):
        return (
            super(ClientsManager, self)
            .get_queryset()
            .prefetch_related("account_manager", "client_manager")
        )


class Client(TimeStampedModel):
    client_name = models.CharField(max_length=255, unique=True)
    account_manager = models.ForeignKey(
        AccountManager,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="account_managers",
    )
    client_manager = models.ManyToManyField(
        ClientManager,
        blank=True,
        related_name="client_managers",
    )

    objects = ClientsManager()

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this client."""
        return reverse("clients:contract_detail", args=[str(self.pk)])
