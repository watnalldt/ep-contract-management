from django.urls import path

from . import views

app_name = "contracts"

urlpatterns = [
    path("contract_list", views.ContractListView.as_view(), name="contract_list"),
    path(
        "contract_detail/<int:pk>/",
        views.ContractDetailView.as_view(),
        name="contract_detail",
    ),
    path("pdf/<pk>", views.contracts_render_pdf_view, name="contract_pdf_view"),
]
