from django.urls import path, register_converter
from .views import IndexTemplateView, AboutTemplateView, ContactTemplateView, ShopTemplateView, CardTemplateView
from .converters import ULIDConverter


register_converter(converter=ULIDConverter, type_name='ulid')


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='shop_index'),
    path('about/', AboutTemplateView.as_view(), name='shop_about'),
    path('contact/', ContactTemplateView.as_view(), name='shop_contact'),
    path('shop/', ShopTemplateView.as_view(), name='shop_list'),
    path('shop/product=<int:item_id>/', CardTemplateView.as_view(), name='card_product')
]

