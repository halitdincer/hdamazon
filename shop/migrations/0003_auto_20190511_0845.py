# Generated by Django 2.2 on 2019-05-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190511_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(upload_to='media/product_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(upload_to='media/product_images/%Y/%m/%d'),
        ),
    ]
