from django.contrib import admin
from expense.models import Expense, ExpenseType

admin.site.register(ExpenseType)
admin.site.register(Expense)
