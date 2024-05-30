from income.views import income_type
from django.urls import path

app_name = "income"

urlpatterns = [
    path("types/", income_type, name="income-type-list")
]
