from django.shortcuts import render
from django.http import HttpResponse

from expense.models import ExpenseType, Expense


def expense_type(request: HttpResponse):
	expenses_type_list = ExpenseType.objects.all()
	context = {
		"type_list": expenses_type_list
	}
	return render(request, "../templates/expense/expenses.html", context)