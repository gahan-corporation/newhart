"""Module for Transaction models."""
from django.db import models

from account.models import Account
# Create your models here.

class Transaction(models.Model):
    """Transaction model class."""
    amount = models.FloatField("Amount")
    left_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_left"
    )
    right_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_right"
    )
    date = models.DateField("Date")
    description = models.TextField("Description")

    def transaction_amount(self):
        """Return amount for transaction."""
        return self.amount

    def transaction_left_account(self):
        """Return the left (credit) account."""
        return self.left_account

    def transaction_right_account(self):
        """Return the right (debit) account."""
        return self.right_account

    def transaction_date(self):
        """Return date of transaction."""
        return self.date

    def transaction_description(self):
        """Return the description."""
        return self.description
