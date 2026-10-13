from django.contrib import admin
from .models import Product, Category
from django.utils.safestring import mark_safe

class ProductAdmin(admin.ModelAdmin):
    # ここに 'image' がないことを確認してください
    list_display = ('id', 'name', 'price', 'category', 'image_preview')
    search_fields = ('name',)
    list_filter = ('category',)

    def image_preview(self, obj):
        # ⚠️ ここが obj.image になっていないか絶対に確認してください
        if obj.img:
            return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.img.url))
        return "画像なし"
    
    image_preview.short_description = '画像Preview'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
