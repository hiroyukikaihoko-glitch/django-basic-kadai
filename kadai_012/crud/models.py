from django.db import models
# どの画面に遷移するのかをModelに指定
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, default='noImage.png')
    # TextFieldで、blank=True, null=True を追加
    detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
