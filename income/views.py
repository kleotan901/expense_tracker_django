from django.shortcuts import render
from django.http import HttpResponse

from income.models import Income, IncomeType


def income_type(request: HttpResponse):
    income_type_list = IncomeType.objects.all()
    context = {
        "type_list": income_type_list
    }
    return render(request, "../templates/income/income.html", context)
