from expense.views import ExpenseListView, ExpenseDetailView
from django.urls import path

app_name = "expense"

urlpatterns = [
    path("transactions/", ExpenseListView.as_view(), name="expense-list"),
    path("transactions/<int:pk>", ExpenseDetailView.as_view(), name="expense-detail")
]
