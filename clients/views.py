# from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView

from contracts.models import Contract

from .models import Client


class ClientListView(ListView):
    model = Client
    template_name = "clients/list.html"
    context_object_name = "clients"
    paginate_by = 5


class ContractDetailView(DetailView):
    model = Client
    template_name = "clients/contracts/all_contracts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contract = Contract.objects.get(pk=self.kwargs["pk"])
        client_contracts = Client.objects.filter(client_name=contract.client_name.id)
        context["client_contracts"] = client_contracts
        return context
