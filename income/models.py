from django.db import models
from django.urls import reverse

from account.models import Account


class IncomeCategory(models.Model):
    category = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Income Categories"

    def __str__(self):
        return self.category


class Income(models.Model):
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    transaction_date = models.DateTimeField("transaction date")
    description = models.CharField(max_length=255, null=True, blank=True,)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        ordering = ("transaction_date",)

    def __str__(self):
        return f"{self.category} - {self.amount}"

    def get_absolute_url(self):
        return reverse("income:income-detail", args=[str(self.pk)])