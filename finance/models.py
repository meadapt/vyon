from django.db import models

# Create your models here.

class Expense(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'expenses'
