from django.contrib import admin

# Register your models here.

from .models import Item, ItemQuantity

admin.site.register(Item)
admin.site.register(ItemQuantity)