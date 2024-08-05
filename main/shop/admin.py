from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_editable = ('slug', )


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('photo', 'title', 'slug', 'description', 'price', 'new_price', 'status', 'category')
    list_editable = ('slug', 'description', 'price', 'new_price', 'status', 'category')
    list_filter = ('category', )
    
    
# @admin.register()
# class IndexAdminChanges(admin.ModelAdmin):
#     pass