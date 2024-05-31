from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from expense.models import ExpenseCategory, Expense


class ExpenseCategoryView(generic.ListView):
	model = ExpenseCategory


class ExpenseListView(generic.ListView):
	model = Expense
	template_name = "expense/expenses.html"
	context_object_name = "expense_list"
	paginate_by = 5


class ExpenseDetailView(generic.DetailView):
	model = Expense
