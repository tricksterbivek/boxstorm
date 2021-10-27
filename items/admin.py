from django.contrib import admin
from items.models.Item_unit import Unit
from items.models.item import Item
from items.models.category import Category

class ItemList(admin.ModelAdmin):
    list_display=['item_name' ,'item_price','category' ,'unit']

class ItemCategory(admin.ModelAdmin):
    list_display=['category_name']

class ItemUnit(admin.ModelAdmin):
    list_display=['unit_name']

admin.site.register(Item,ItemList)
admin.site.register(Category,ItemCategory)
admin.site.register(Unit,ItemUnit)