from django.contrib import admin

from .models import Category, Product, IndexTemplateSlide, TemplateContent

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_editable = ('slug', )


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'slug', 'description', 'price', 'new_price', 'status', 'category')
    list_editable = ('slug', 'description', 'price', 'new_price', 'status', 'category')
    list_filter = ('category', )
    
    
@admin.register(IndexTemplateSlide)
class IndexAdminChanges(admin.ModelAdmin):
    pass

@admin.register(TemplateContent)
class IndexAdminContent(admin.ModelAdmin):
    pass