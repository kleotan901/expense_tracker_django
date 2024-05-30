from expense.views import expense_type
from django.urls import path

app_name = "expense"

urlpatterns = [
    path("types/", expense_type, name="expense-type-list")
]