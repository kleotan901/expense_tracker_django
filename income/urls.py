from income.views import IncomeView
from django.urls import path

app_name = "income"

urlpatterns = [
    path("types/", IncomeView.as_view(), name="income-list")
]
