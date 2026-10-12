from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView # 💡 1行にまとめました
from .models import Product

# 使わない以下のインポート文はすべて削除しました：
# - CreateView, UpdateView, DeleteView
# - reverse_lazy
# Create your views here.

class TopView(TemplateView):
    template_name = "top.html"

# 商品一覧
class ProductListView(ListView):
    model = Product
    paginate_by = 3  # 1ページに3件ずつ表示

# 商品詳細
class ProductDetailView(DetailView):
    model = Product
    template_name = "crud/product_detail.html"
