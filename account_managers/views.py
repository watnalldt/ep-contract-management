from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import ListView

from clients.models import Client
from core.decorators import account_manager_required
from core.views import HTMLTitleMixin

User = get_user_model()


@method_decorator([never_cache, account_manager_required], name="dispatch")
class AccountManagerListView(LoginRequiredMixin, HTMLTitleMixin, ListView):
    model = Client
    template_name = "account_managers/dashboard.html"
    html_title = "Account Manager Dashboard"

    def get_queryset(self):
        return Client.objects.filter(
            account_manager__account_manager=self.request.user.id
        )
