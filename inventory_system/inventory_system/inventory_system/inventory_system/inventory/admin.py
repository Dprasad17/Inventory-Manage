from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'sold')  # Columns to show in admin

admin.site.site_header = "Inventory Control Management"
admin.site.site_title = "Inventory Control Management"
admin.site.index_title = "Welcome to Inventory Dashboard"