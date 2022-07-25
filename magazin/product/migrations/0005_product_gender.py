# Generated by Django 4.0.5 on 2022-07-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_full_price_alter_product_price_now'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('Male', 'Мужчины'), ('Female', 'Женщины'), ('Unisex', 'Унисекс')], default='Unisex', max_length=120, verbose_name='Гендер'),
        ),
    ]
