# Generated by Django 5.0.7 on 2024-08-05 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_indextemplateslide_templatecontent_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='templatecontent',
            options={'verbose_name': 'контент', 'verbose_name_plural': 'Заголовки главной страницы'},
        ),
        migrations.AlterModelTable(
            name='templatecontent',
            table='index_content',
        ),
    ]