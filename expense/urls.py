from expense.views import ExpenseView
from django.urls import path

app_name = "expense"

urlpatterns = [
    path("types/", ExpenseView.as_view(), name="expense-list")
]
