from django.contrib import admin
from .models import Product
# 一覧表示
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)

# Register your models here.
# admin.site.register(Product)
# 一覧表示
admin.site.register(Product, ProductAdmin)
