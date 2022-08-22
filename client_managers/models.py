from django.conf import settings
from django.db import models


class ClientManager(models.Model):
    client_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="client_contacts",
    )

    class Meta:
        verbose_name = "Client Manager"
        verbose_name_plural = "Client Managers"

    def __str__(self):
        return str(self.client_manager)
