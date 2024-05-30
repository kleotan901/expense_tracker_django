from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from expense.models import ExpenseType, Expense


class ExpenseTypeView(generic.ListView):
	model = ExpenseType


class ExpenseView(generic.ListView):
	model = Expense
	template_name = "expense/expenses.html"
	context_object_name = "expense_list"

