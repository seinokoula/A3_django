from django.contrib import admin

# Register your models here.

from .models import Items

class ItemsAdmin(admin.ModelAdmin):
    fields = ['item_name', 'item_price', 'item_stock', 'item_image']

admin.site.register(Items)