from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=24, unique=True, blank=False, editable=True, null=False)
    slug = models.SlugField(max_length=24, unique=True, blank=False, null=False)


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
    title = models.CharField(max_length=128, editable=True)
    slug = models.SlugField(max_length=128)
    description = models.TextField(editable=True)
    price = models.IntegerField(editable=True)
    new_price = models.IntegerField(editable=True)
    photo = models.ImageField(editable=True)
    status = models.CharField(max_length=18, editable=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, db_index=True)

    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'изделие'
        verbose_name_plural = 'изделия'