from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from .models import Category, Item

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_sold", "created_by", "created_at")
    list_filter = ("category", "is_sold")
    search_fields = ("name", "description")

# Register safely
try:
    admin.site.register(Category, CategoryAdmin)
except AlreadyRegistered:
    admin.site.unregister(Category)
    admin.site.register(Category, CategoryAdmin)

try:
    admin.site.register(Item, ItemAdmin)
except AlreadyRegistered:
    admin.site.unregister(Item)
    admin.site.register(Item, ItemAdmin)
