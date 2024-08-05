from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=24, unique=True, blank=False, editable=True, null=False, db_comment="Название категории")
    slug = models.SlugField(max_length=24, unique=True, blank=False, null=False, db_comment="слаг(название категории на английском)")


    def __str__(self):
        return self.name
    
    class Meta:
        abstract: bool
        app_label: str
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name', )
        db_table: str   
    

class Product(models.Model):
    title = models.CharField(max_length=128, editable=True, blank=False, null=False, db_comment="название изделия")
    slug = models.SlugField(max_length=128, blank=False, null=False, db_comment="слаг (название изделия на английском)")
    description = models.TextField(editable=True, blank=False, null=False, db_comment="описание изделия")
    price = models.IntegerField(editable=True, blank=False, null=False, db_comment="цена")
    new_price = models.IntegerField(editable=True, blank=True, null=False, db_comment="новая цена(при уценке или дорожании)")
    photo = models.ImageField(editable=True, blank=False, null=False)
    status = models.CharField(max_length=18, editable=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, db_index=True)

    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'изделие'
        verbose_name_plural = 'изделия'
        
        
class IndexTemplateSlide(models.Model):
    title_slider = models.CharField(max_length=64, editable=True, blank=False, null=False, db_comment="текст акции на слайдере")
    body_slider = models.CharField(max_length=128, editable=True, blank=False, null=False, db_comment="описание акции на слайдере")
    photo_slider = models.ImageField(editable=True, help_text="фотография для слайдера в последнем блоке")
    
    def __str__(self):
        return self.title_slider
    
    class Meta:
        verbose_name = 'контент'
        verbose_name_plural = 'слайдеры'
        db_table = 'index_slider'


class IndexTemplateContent(models.Model):
    important_title = models.CharField(max_length=20, editable=True)