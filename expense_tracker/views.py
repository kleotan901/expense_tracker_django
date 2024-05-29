from django.db.models import Sum
from django.shortcuts import render
from django.http import HttpResponse

from expense.models import Expense
from income.models import Income


def index(request: HttpResponse):
    expense_list = Expense.objects.all()
    income_list = Income.objects.all()
    total_expense_sum = expense_list.aggregate(Sum("amount"))["amount__sum"]
    total_income_sum = income_list.aggregate(Sum("amount"))["amount__sum"]
    context = {
        "expense_list": expense_list,
        "income_list": income_list,
        "total_expense_sum": total_expense_sum,
        "total_income_sum": total_income_sum
    }
    return render(request, "../templates/index.html", context)
