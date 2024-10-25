from django.contrib import admin
from .models import (
    Expense,
    Category
)

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category, CategoryAdmin)
