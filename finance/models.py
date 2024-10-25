from django.db import models
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    value = models.FloatField(validators=[MinValueValidator(0.01)])
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(null = True, blank = True)

    class Meta:
        db_table = 'expenses'

    def __str__(self):
        return self.name
