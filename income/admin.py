from django.contrib import admin
from income.models import Income, IncomeType

admin.site.register(IncomeType)
admin.site.register(Income)