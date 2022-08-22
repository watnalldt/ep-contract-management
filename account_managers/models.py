from django.conf import settings
from django.db import models


class AccountManager(models.Model):
    account_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Account Manager"
        verbose_name_plural = "Account Managers"

    def __str__(self):
        return f"{self.account_manager}"
