from django.contrib import admin
from .models import Page

# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ["id", "source", "correct", "incorrect_1", "incorrect_2"]