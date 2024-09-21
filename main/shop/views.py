from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, TemplateView, DetailView
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.http import require_GET
from .models import Category, Product, IndexTemplateSlide, TemplateContent


class IndexTemplateView(TemplateView):
    template_name = 'shop/index.html'
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sweatshirt_category = Category.objects.get(slug='sweetshot')
        tshirt_category = Category.objects.get(slug='t-shirt')
        long_category = Category.objects.get(slug='longsleeve')
        
        context['sweetshot'] = Product.objects.select_related('category').filter(category=sweatshirt_category).order_by('-id')[:3]
        context['tshirt'] = Product.objects.select_related('category').filter(category=tshirt_category).order_by('-id')[:3]
        context['longsleeve'] = Product.objects.select_related('category').filter(category=long_category).order_by('-id')[:3]
        
        context['sliders'] = IndexTemplateSlide.objects.all()
        context['content'] = TemplateContent.objects.get()
        return context
    
    

class AboutTemplateView(TemplateView):
    template_name = 'shop/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_title'] = None
        return context
    


class ContactTemplateView(TemplateView):
    template_name = 'shop/contact.html'


class ShopTemplateView(ListView):
    template_name = 'shop/shop.html'
    model = Product
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = list(Category.objects.all())
        categories.insert(0, 'Все')
        category_map = {}
        category_map['Все'] = Product.objects.all()
        for category in categories:
            if isinstance(category, Category):
                category_map.update({category.name: Product.objects.filter(category__slug=category.slug)})    
        context["categories"] = categories
        context['category_map'] = category_map.values()
        return context
    

class CardTemplateView(DetailView):
    model = Product
    template_name = 'shop/detail.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
