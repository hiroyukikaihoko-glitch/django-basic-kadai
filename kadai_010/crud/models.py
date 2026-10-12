from django.db import models
# どの画面に遷移するのかをModelに指定
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('list')