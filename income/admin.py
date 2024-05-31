from django.contrib import admin
from income.models import Income, IncomeCategory

admin.site.register(IncomeCategory)
admin.site.register(Income)