# Generated by Django 4.0.5 on 2022-08-06 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_favorite_products_favoriteuserproduct'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_product_cart', to='product.product', verbose_name='Товар'),
        ),
    ]
