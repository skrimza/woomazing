from django.views.generic import ListView, TemplateView, DetailView

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
        context["categories"] = categories
        sweatshirt_category = Category.objects.get(slug='sweetshot')
        tshirt_category = Category.objects.get(slug='t-shirt')
        long_category = Category.objects.get(slug='longsleeve')
        products = Product.objects.select_related('category').all()
        context['all_products'] = products
        context['sweetshot'] = [product for product in products if product.category == sweatshirt_category]
        context['tshirt'] = [product for product in products if product.category == tshirt_category]
        context['longsleeve'] = [product for product in products if product.category == long_category]
        return context
    
    def get_queryset(self):
        pass
        # superset = super().get_queryset()  
    

class ProductTemplateView(DetailView):
    pass