# Generated by Django 4.0.5 on 2022-08-14 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_favorite_products_favoriteuserproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=255, verbose_name='Название акции')),
                ('image_stock', models.ImageField(blank=True, default='product/system_img/default.jpg', upload_to='stock/%Y/%m/%d/', verbose_name='Банер акции')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_in_stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_in_stock', to='product.productstock', verbose_name='В акции'),
        ),
    ]
