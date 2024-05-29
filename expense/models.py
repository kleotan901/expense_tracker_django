from django.db import models
from account.models import Account


class ExpenseType(models.Model):
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.source


class Expense(models.Model):
    source = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    currency = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name="account")
    transaction_date = models.DateTimeField("transaction date")
    description = models.CharField(max_length=255, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        ordering = ("transaction_date", )

    def __str__(self):
        return f"{self.source} - {self.amount}"