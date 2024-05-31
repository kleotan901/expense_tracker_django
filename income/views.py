from django.views import generic
from income.models import Income, IncomeCategory


class IncomeCategoryView(generic.ListView):
    model = IncomeCategory


class IncomeListView(generic.ListView):
    model = Income
    template_name = "income/income.html"
    context_object_name = "income_list"
    paginate_by = 5


class IncomeDetailView(generic.DetailView):
    model = Income
