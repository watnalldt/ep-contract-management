from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path("client_list/", views.ClientListView.as_view(), name="client_list"),
    path(
        "contract_detail/<int:pk>/",
        views.ContractDetailView.as_view(),
        name="contract_detail",
    ),
]
