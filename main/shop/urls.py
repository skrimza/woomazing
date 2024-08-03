from django.urls import path, register_converter

from .views import IndexTemplateView
from .converters import ULIDConverter


register_converter(converter=ULIDConverter, type_name='ulid')


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='shop_index')
]