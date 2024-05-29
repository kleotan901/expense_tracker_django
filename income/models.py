from django.db import models
from account.models import Account


class IncomeType(models.Model):
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.source


class Income(models.Model):
    source = models.ForeignKey(IncomeType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    transaction_date = models.DateTimeField("transaction date")
    description = models.CharField(max_length=255, null=True, blank=True,)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        ordering = ("transaction_date",)

    def __str__(self):
        return f"{self.source} - {self.amount}"
