# Generated by Django 5.0.7 on 2024-08-09 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_indextemplateslide_body_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indextemplateslide',
            name='photo_slider',
            field=models.ImageField(help_text='фотография для слайдера в последнем блоке', upload_to='slides/'),
        ),
    ]