from django.db import models
from django.urls import reverse

from account.models import Account


class ExpenseCategory(models.Model):
    category = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Expense Categories"

    def __str__(self):
        return self.category


class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    transaction_date = models.DateTimeField("transaction date")
    description = models.CharField(max_length=255, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ("transaction_date", )

    def __str__(self):
        return f"{self.category} - {self.amount}"

    def get_absolute_url(self):
        return reverse("expense:expense-detail", args=[str(self.pk)])
