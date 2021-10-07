from django.contrib import admin
# Import Item class model from Todo models.py
from .models import Item
# Register your models here.
admin.site.register(Item)
