from django.contrib import admin
from .models import Custumer

# Register your models here.

@admin.register(Custumer)
class CustumerAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email"]

