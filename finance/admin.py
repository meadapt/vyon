from django.contrib import admin
from .models import (
    Expense,
    Owner,
    Category,
    ExpenseOwner,
)

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class OwnerAdmin(admin.ModelAdmin):
    pass

class ExpenseOwnerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ExpenseOwner, CategoryAdmin)
