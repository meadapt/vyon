from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    owners = models.ManyToManyField(Owner, through='ExpenseOwner')
    estimated_value = models.FloatField(validators=[MinValueValidator(0.01)])
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(null = True, blank = True)

    class Meta:
        db_table = 'expenses'

    def __str__(self):
        return self.name

class ExpenseOwner(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.RESTRICT)
    owner = models.ForeignKey(Owner, on_delete=models.RESTRICT)
    percentage = models.FloatField(
        validators=[
            MinValueValidator(0.01),
            MaxValueValidator(100.00),
            ]
        )

    class Meta:
        db_table = 'expense_owners'

    def __str__(self):
        return f'{self.expense} - {self.owner} - {self.percentage}'
