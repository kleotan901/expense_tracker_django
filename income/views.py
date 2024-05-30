from django.views import generic

from income.models import Income, IncomeType


class IncomeTypeView(generic.ListView):
    model = IncomeType


class IncomeView(generic.ListView):
    model = Income
    template_name = "income/income.html"
    context_object_name = "income_list"
