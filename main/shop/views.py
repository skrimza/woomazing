from django.views.generic import ListView, TemplateView

from .models import Category, Product


class IndexTemplateView(TemplateView):
    template_name = 'shop/index.html'
    model = Category
    
