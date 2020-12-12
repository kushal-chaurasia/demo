from django.contrib import admin
from .models import Card

# Register your models here.
@admin.register(Card)
class CardDetail (admin.ModelAdmin):
    list_display = ['id', 'name', 'card_no','expiry','cvv']
