from income.views import IncomeListView, IncomeDetailView
from django.urls import path

app_name = "income"

urlpatterns = [
    path("transactions/", IncomeListView.as_view(), name="income-list"),
    path("transactions/<int:pk>", IncomeDetailView.as_view(), name="income-detail")
]
