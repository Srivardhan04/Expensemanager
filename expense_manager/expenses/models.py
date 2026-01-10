from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    TYPE_CHOICES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.FloatField()

    date = models.DateField()
    note = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.type}) ₹{self.amount}"
    
    class Meta:
        ordering = ['-date']   # newest first
