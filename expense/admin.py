from django.contrib import admin
from expense.models import Expense, ExpenseCategory

admin.site.register(ExpenseCategory)
admin.site.register(Expense)
