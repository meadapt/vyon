from django.db import models

# Create your models here.

class Despesa(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'despesas'
