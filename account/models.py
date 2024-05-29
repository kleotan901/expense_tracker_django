from django.db import models


class Account(models.Model):
    number = models.IntegerField()
    currency = models.CharField(max_length=3)
    bank_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.number} {self.currency}"
